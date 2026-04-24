#!/usr/bin/env python3

import math

import rclpy
from geometry_msgs.msg import TransformStamped, Twist
from nav_msgs.msg import Odometry
from rclpy.duration import Duration
from rclpy.node import Node
from sensor_msgs.msg import JointState, LaserScan
from std_srvs.srv import Trigger
from tf2_ros import TransformBroadcaster


class CmdVelDriveNode(Node):
    def __init__(self):
        super().__init__("cmd_vel_drive")

        self.declare_parameter("publish_rate", 30.0)
        self.declare_parameter("wheel_radius", 0.08)
        self.declare_parameter("wheel_separation", 0.38)
        self.declare_parameter("cmd_timeout", 0.5)
        self.declare_parameter("max_linear_speed", 0.8)
        self.declare_parameter("max_angular_speed", 1.5)
        self.declare_parameter("max_linear_accel", 1.0)
        self.declare_parameter("max_angular_accel", 2.5)
        self.declare_parameter("enable_safety_stop", True)
        self.declare_parameter("enable_safety_slowdown", True)
        self.declare_parameter("safety_stop_distance", 0.18)
        self.declare_parameter("safety_slow_distance", 0.80)
        self.declare_parameter("safety_angle", 0.45)
        self.declare_parameter("enable_auto_avoid", True)
        self.declare_parameter("auto_avoid_max_turn_speed", 0.9)
        self.declare_parameter("auto_avoid_gain", 2.0)
        self.declare_parameter("front_body_offset", 0.13)
        self.declare_parameter("rear_body_offset", 0.38)

        self.publish_rate = float(self.get_parameter("publish_rate").value)
        self.wheel_radius = float(self.get_parameter("wheel_radius").value)
        self.wheel_separation = float(self.get_parameter("wheel_separation").value)
        self.cmd_timeout = float(self.get_parameter("cmd_timeout").value)
        self.max_linear_speed = float(self.get_parameter("max_linear_speed").value)
        self.max_angular_speed = float(self.get_parameter("max_angular_speed").value)
        self.max_linear_accel = float(self.get_parameter("max_linear_accel").value)
        self.max_angular_accel = float(self.get_parameter("max_angular_accel").value)
        self.enable_safety_stop = bool(self.get_parameter("enable_safety_stop").value)
        self.enable_safety_slowdown = bool(
            self.get_parameter("enable_safety_slowdown").value
        )
        self.safety_stop_distance = float(
            self.get_parameter("safety_stop_distance").value
        )
        self.safety_slow_distance = float(
            self.get_parameter("safety_slow_distance").value
        )
        self.safety_angle = float(self.get_parameter("safety_angle").value)
        self.enable_auto_avoid = bool(self.get_parameter("enable_auto_avoid").value)
        self.auto_avoid_max_turn_speed = float(
            self.get_parameter("auto_avoid_max_turn_speed").value
        )
        self.auto_avoid_gain = float(self.get_parameter("auto_avoid_gain").value)
        self.front_body_offset = float(self.get_parameter("front_body_offset").value)
        self.rear_body_offset = float(self.get_parameter("rear_body_offset").value)

        self.target_linear = 0.0
        self.target_angular = 0.0
        self.current_linear = 0.0
        self.current_angular = 0.0
        self.last_cmd_time = self.get_clock().now()

        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.left_wheel_position = 0.0
        self.right_wheel_position = 0.0
        self.last_update_time = self.get_clock().now()

        self.front_min_range = float("inf")
        self.rear_min_range = float("inf")
        self.front_left_min_range = float("inf")
        self.front_right_min_range = float("inf")
        self.obstacle_blocked = False

        self.cmd_subscription = self.create_subscription(
            Twist, "/cmd_vel", self.cmd_vel_callback, 10
        )
        self.scan_subscription = self.create_subscription(
            LaserScan, "/scan", self.scan_callback, 10
        )
        self.reset_service = self.create_service(
            Trigger, "/reset_odometry", self.reset_odometry_callback
        )
        self.joint_publisher = self.create_publisher(JointState, "/joint_states", 10)
        self.odom_publisher = self.create_publisher(Odometry, "/odom", 10)
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(1.0 / self.publish_rate, self.update_and_publish)

        self.get_logger().info(
            "cmd_vel_drive started: "
            f"publish_rate={self.publish_rate:.1f} Hz, "
            f"wheel_radius={self.wheel_radius:.2f} m, "
            f"wheel_separation={self.wheel_separation:.2f} m, "
            f"cmd_timeout={self.cmd_timeout:.2f} s, "
            f"max_linear_speed={self.max_linear_speed:.2f} m/s, "
            f"max_angular_speed={self.max_angular_speed:.2f} rad/s, "
            f"enable_safety_stop={self.enable_safety_stop}, "
            f"enable_safety_slowdown={self.enable_safety_slowdown}, "
            f"enable_auto_avoid={self.enable_auto_avoid}"
        )

    def cmd_vel_callback(self, msg):
        self.target_linear = self.clamp(
            float(msg.linear.x), -self.max_linear_speed, self.max_linear_speed
        )
        self.target_angular = self.clamp(
            float(msg.angular.z), -self.max_angular_speed, self.max_angular_speed
        )
        self.last_cmd_time = self.get_clock().now()

    def scan_callback(self, msg):
        front_min_range = float("inf")
        rear_min_range = float("inf")
        front_left_min_range = float("inf")
        front_right_min_range = float("inf")

        for index, range_value in enumerate(msg.ranges):
            if not math.isfinite(range_value):
                continue

            angle = msg.angle_min + index * msg.angle_increment
            if not (msg.range_min <= range_value <= msg.range_max):
                continue

            if abs(angle) <= self.safety_angle:
                front_min_range = min(front_min_range, range_value)
                if angle >= 0.0:
                    front_left_min_range = min(front_left_min_range, range_value)
                else:
                    front_right_min_range = min(front_right_min_range, range_value)

            rear_angle_error = min(abs(angle - math.pi), abs(angle + math.pi))
            if rear_angle_error <= self.safety_angle:
                rear_min_range = min(rear_min_range, range_value)

        self.front_min_range = front_min_range
        self.rear_min_range = rear_min_range
        self.front_left_min_range = front_left_min_range
        self.front_right_min_range = front_right_min_range

        front_blocked = (
            self.compute_clearance(front_min_range, self.front_body_offset)
            < self.safety_stop_distance
        )
        rear_blocked = (
            self.compute_clearance(rear_min_range, self.rear_body_offset)
            < self.safety_stop_distance
        )
        blocked_now = front_blocked or rear_blocked

        if blocked_now != self.obstacle_blocked:
            self.obstacle_blocked = blocked_now
            if blocked_now:
                if front_blocked:
                    self.get_logger().warn(
                        "Safety stop active: front clearance %.2f m"
                        % self.compute_clearance(
                            self.front_min_range, self.front_body_offset
                        )
                    )
                else:
                    self.get_logger().warn(
                        "Safety stop active: rear clearance %.2f m"
                        % self.compute_clearance(
                            self.rear_min_range, self.rear_body_offset
                        )
                    )
            else:
                self.get_logger().info("Safety stop cleared")

    def update_and_publish(self):
        now = self.get_clock().now()
        dt = (now - self.last_update_time).nanoseconds / 1e9
        self.last_update_time = now
        if dt <= 0.0:
            return

        command_linear = self.target_linear
        command_angular = self.target_angular

        linear_target = command_linear
        angular_target = command_angular

        if now - self.last_cmd_time > Duration(seconds=self.cmd_timeout):
            linear_target = 0.0
            angular_target = 0.0

        linear_target = self.apply_lidar_safety(linear_target)
        angular_target = self.apply_auto_avoidance(
            linear_target, angular_target, command_linear
        )

        self.current_linear = self.step_towards(
            self.current_linear, linear_target, self.max_linear_accel * dt
        )
        self.current_angular = self.step_towards(
            self.current_angular, angular_target, self.max_angular_accel * dt
        )

        self.x += self.current_linear * math.cos(self.yaw) * dt
        self.y += self.current_linear * math.sin(self.yaw) * dt
        self.yaw += self.current_angular * dt

        left_wheel_velocity = (
            self.current_linear - self.current_angular * self.wheel_separation / 2.0
        ) / self.wheel_radius
        right_wheel_velocity = (
            self.current_linear + self.current_angular * self.wheel_separation / 2.0
        ) / self.wheel_radius

        self.left_wheel_position += left_wheel_velocity * dt
        self.right_wheel_position += right_wheel_velocity * dt

        self.publish_joint_states(now, left_wheel_velocity, right_wheel_velocity)
        self.publish_odom(now, self.current_linear, self.current_angular)
        self.publish_transform(now)

    def apply_lidar_safety(self, linear_target):
        if linear_target > 0.0:
            return self.limit_linear_target_by_range(
                linear_target, self.front_min_range, self.front_body_offset, "front"
            )

        if linear_target < 0.0:
            limited = self.limit_linear_target_by_range(
                abs(linear_target), self.rear_min_range, self.rear_body_offset, "rear"
            )
            return -limited

        return 0.0

    def apply_auto_avoidance(self, linear_target, angular_target, command_linear):
        if not self.enable_auto_avoid:
            return angular_target
        if command_linear <= 0.0:
            return angular_target

        front_clearance = self.compute_clearance(
            self.front_min_range, self.front_body_offset
        )
        if not math.isfinite(front_clearance):
            return angular_target
        if front_clearance >= self.safety_slow_distance:
            return angular_target

        front_left_clearance = self.compute_clearance(
            self.front_left_min_range, self.front_body_offset
        )
        front_right_clearance = self.compute_clearance(
            self.front_right_min_range, self.front_body_offset
        )
        if not math.isfinite(front_left_clearance):
            front_left_clearance = self.safety_slow_distance
        if not math.isfinite(front_right_clearance):
            front_right_clearance = self.safety_slow_distance

        slowdown_span = max(
            self.safety_slow_distance - self.safety_stop_distance, 1e-6
        )
        proximity_ratio = 1.0 - self.clamp(
            (front_clearance - self.safety_stop_distance) / slowdown_span,
            0.0,
            1.0,
        )
        clearance_error = front_left_clearance - front_right_clearance
        avoid_turn = self.auto_avoid_gain * clearance_error * proximity_ratio
        avoid_turn = self.clamp(
            avoid_turn,
            -self.auto_avoid_max_turn_speed,
            self.auto_avoid_max_turn_speed,
        )

        return self.clamp(
            angular_target + avoid_turn,
            -self.max_angular_speed,
            self.max_angular_speed,
        )

    def limit_linear_target_by_range(
        self, target_speed, obstacle_range, body_offset, direction_label
    ):
        clearance = self.compute_clearance(obstacle_range, body_offset)
        if not math.isfinite(clearance):
            return target_speed

        if self.enable_safety_stop and clearance <= self.safety_stop_distance:
            return 0.0
        if not self.enable_safety_slowdown:
            return target_speed
        if clearance >= self.safety_slow_distance:
            return target_speed

        slowdown_span = self.safety_slow_distance - self.safety_stop_distance
        if slowdown_span <= 1e-6:
            return 0.0

        ratio = (clearance - self.safety_stop_distance) / slowdown_span
        ratio = self.clamp(ratio, 0.0, 1.0)
        limited_speed = target_speed * ratio

        if limited_speed < target_speed:
            self.get_logger().debug(
                "Safety slowdown (%s): clearance=%.2f m, target=%.2f m/s, limited=%.2f m/s"
                % (direction_label, clearance, target_speed, limited_speed)
            )

        return limited_speed

    def publish_joint_states(self, now, left_wheel_velocity, right_wheel_velocity):
        msg = JointState()
        msg.header.stamp = now.to_msg()
        msg.name = ["left_wheel_joint", "right_wheel_joint"]
        msg.position = [self.left_wheel_position, self.right_wheel_position]
        msg.velocity = [left_wheel_velocity, right_wheel_velocity]
        self.joint_publisher.publish(msg)

    def publish_odom(self, now, linear_speed, angular_speed):
        msg = Odometry()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = "odom"
        msg.child_frame_id = "base_footprint"
        msg.pose.pose.position.x = self.x
        msg.pose.pose.position.y = self.y
        msg.pose.pose.position.z = 0.0
        msg.pose.pose.orientation.z = math.sin(self.yaw / 2.0)
        msg.pose.pose.orientation.w = math.cos(self.yaw / 2.0)
        msg.twist.twist.linear.x = linear_speed
        msg.twist.twist.angular.z = angular_speed
        self.odom_publisher.publish(msg)

    def publish_transform(self, now):
        transform = TransformStamped()
        transform.header.stamp = now.to_msg()
        transform.header.frame_id = "odom"
        transform.child_frame_id = "base_footprint"
        transform.transform.translation.x = self.x
        transform.transform.translation.y = self.y
        transform.transform.translation.z = 0.0
        transform.transform.rotation.z = math.sin(self.yaw / 2.0)
        transform.transform.rotation.w = math.cos(self.yaw / 2.0)
        self.tf_broadcaster.sendTransform(transform)

    def reset_odometry_callback(self, _request, response):
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.current_linear = 0.0
        self.current_angular = 0.0
        self.left_wheel_position = 0.0
        self.right_wheel_position = 0.0
        self.target_linear = 0.0
        self.target_angular = 0.0
        self.last_cmd_time = self.get_clock().now()
        self.last_update_time = self.get_clock().now()
        self.front_min_range = float("inf")
        self.rear_min_range = float("inf")
        self.front_left_min_range = float("inf")
        self.front_right_min_range = float("inf")
        self.obstacle_blocked = False
        response.success = True
        response.message = "Odometry and wheel positions have been reset."
        self.get_logger().info(response.message)
        return response

    @staticmethod
    def clamp(value, min_value, max_value):
        return max(min_value, min(value, max_value))

    @staticmethod
    def compute_clearance(obstacle_range, body_offset):
        if not math.isfinite(obstacle_range):
            return float("inf")
        return max(0.0, obstacle_range - body_offset)

    @staticmethod
    def step_towards(current_value, target_value, max_step):
        delta = target_value - current_value
        if abs(delta) <= max_step:
            return target_value
        return current_value + math.copysign(max_step, delta)


def main():
    rclpy.init()
    node = CmdVelDriveNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
