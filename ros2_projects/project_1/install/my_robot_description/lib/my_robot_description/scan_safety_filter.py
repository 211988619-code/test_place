#!/usr/bin/env python3

import math

import rclpy
from geometry_msgs.msg import Twist
from my_robot_description.msg import SafetyDebug
from rclpy.duration import Duration
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class ScanSafetyFilterNode(Node):
    def __init__(self):
        super().__init__("scan_safety_filter")

        self.declare_parameter("input_topic", "/cmd_vel_input")
        self.declare_parameter("output_topic", "/cmd_vel")
        self.declare_parameter("debug_topic", "/safety_debug")
        self.declare_parameter("cmd_timeout", 0.5)
        self.declare_parameter("publish_rate", 20.0)
        self.declare_parameter("enable_safety_stop", True)
        self.declare_parameter("enable_safety_slowdown", True)
        self.declare_parameter("enable_auto_avoid", False)
        self.declare_parameter("safety_stop_distance", 0.18)
        self.declare_parameter("safety_slow_distance", 0.80)
        self.declare_parameter("safety_angle", 0.45)
        self.declare_parameter("auto_avoid_max_turn_speed", 0.6)
        self.declare_parameter("auto_avoid_gain", 1.5)
        self.declare_parameter("front_body_offset", 0.13)
        self.declare_parameter("rear_body_offset", 0.38)
        self.declare_parameter("max_linear_speed", 0.8)
        self.declare_parameter("max_angular_speed", 1.5)

        input_topic = str(self.get_parameter("input_topic").value)
        output_topic = str(self.get_parameter("output_topic").value)
        self.debug_topic = str(self.get_parameter("debug_topic").value)
        self.cmd_timeout = float(self.get_parameter("cmd_timeout").value)
        self.publish_rate = float(self.get_parameter("publish_rate").value)
        self.enable_safety_stop = bool(
            self.get_parameter("enable_safety_stop").value
        )
        self.enable_safety_slowdown = bool(
            self.get_parameter("enable_safety_slowdown").value
        )
        self.enable_auto_avoid = bool(self.get_parameter("enable_auto_avoid").value)
        self.safety_stop_distance = float(
            self.get_parameter("safety_stop_distance").value
        )
        self.safety_slow_distance = float(
            self.get_parameter("safety_slow_distance").value
        )
        self.safety_angle = float(self.get_parameter("safety_angle").value)
        self.auto_avoid_max_turn_speed = float(
            self.get_parameter("auto_avoid_max_turn_speed").value
        )
        self.auto_avoid_gain = float(self.get_parameter("auto_avoid_gain").value)
        self.front_body_offset = float(self.get_parameter("front_body_offset").value)
        self.rear_body_offset = float(self.get_parameter("rear_body_offset").value)
        self.max_linear_speed = float(self.get_parameter("max_linear_speed").value)
        self.max_angular_speed = float(self.get_parameter("max_angular_speed").value)

        self.target_linear = 0.0
        self.target_angular = 0.0
        self.last_cmd_time = self.get_clock().now()
        self.front_min_range = float("inf")
        self.rear_min_range = float("inf")
        self.front_left_min_range = float("inf")
        self.front_right_min_range = float("inf")
        self.obstacle_blocked = False

        self.cmd_subscription = self.create_subscription(
            Twist, input_topic, self.cmd_callback, 10
        )
        self.scan_subscription = self.create_subscription(
            LaserScan, "/scan", self.scan_callback, 10
        )
        self.cmd_publisher = self.create_publisher(Twist, output_topic, 10)
        self.debug_publisher = self.create_publisher(
            SafetyDebug, self.debug_topic, 10
        )
        self.timer = self.create_timer(1.0 / self.publish_rate, self.publish_filtered)

        self.get_logger().info(
            "scan_safety_filter started: "
            f"input_topic={input_topic}, output_topic={output_topic}, "
            f"enable_safety_stop={self.enable_safety_stop}, "
            f"enable_safety_slowdown={self.enable_safety_slowdown}, "
            f"enable_auto_avoid={self.enable_auto_avoid}"
        )

    def cmd_callback(self, msg):
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
        self.obstacle_blocked = front_blocked or rear_blocked

    def publish_filtered(self):
        now = self.get_clock().now()
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

        cmd = Twist()
        cmd.linear.x = float(linear_target)
        cmd.angular.z = float(angular_target)
        self.cmd_publisher.publish(cmd)
        self.publish_debug(now, command_linear, command_angular, linear_target, angular_target)

    def apply_lidar_safety(self, linear_target):
        if linear_target > 0.0:
            return self.limit_linear_target_by_range(
                linear_target, self.front_min_range, self.front_body_offset
            )
        if linear_target < 0.0:
            limited = self.limit_linear_target_by_range(
                abs(linear_target), self.rear_min_range, self.rear_body_offset
            )
            return -limited
        return 0.0

    def apply_auto_avoidance(self, linear_target, angular_target, command_linear):
        if not self.enable_auto_avoid or command_linear <= 0.0:
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

    def limit_linear_target_by_range(self, target_speed, obstacle_range, body_offset):
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
        return target_speed * self.clamp(ratio, 0.0, 1.0)

    def publish_debug(
        self, now, command_linear, command_angular, linear_target, angular_target
    ):
        front_clearance = self.compute_clearance(
            self.front_min_range, self.front_body_offset
        )
        rear_clearance = self.compute_clearance(
            self.rear_min_range, self.rear_body_offset
        )
        front_left_clearance = self.compute_clearance(
            self.front_left_min_range, self.front_body_offset
        )
        front_right_clearance = self.compute_clearance(
            self.front_right_min_range, self.front_body_offset
        )

        msg = SafetyDebug()
        msg.stamp = now.to_msg()
        msg.cmd_linear = self.debug_value(command_linear)
        msg.cmd_angular = self.debug_value(command_angular)
        msg.target_linear_after_safety = self.debug_value(linear_target)
        msg.target_angular_after_avoid = self.debug_value(angular_target)
        msg.current_linear = self.debug_value(linear_target)
        msg.current_angular = self.debug_value(angular_target)
        msg.front_range = self.debug_value(self.front_min_range)
        msg.rear_range = self.debug_value(self.rear_min_range)
        msg.front_left_range = self.debug_value(self.front_left_min_range)
        msg.front_right_range = self.debug_value(self.front_right_min_range)
        msg.front_clearance = self.debug_value(front_clearance)
        msg.rear_clearance = self.debug_value(rear_clearance)
        msg.front_left_clearance = self.debug_value(front_left_clearance)
        msg.front_right_clearance = self.debug_value(front_right_clearance)
        msg.obstacle_blocked = self.obstacle_blocked
        self.debug_publisher.publish(msg)

    @staticmethod
    def compute_clearance(obstacle_range, body_offset):
        if not math.isfinite(obstacle_range):
            return float("inf")
        return max(0.0, obstacle_range - body_offset)

    @staticmethod
    def clamp(value, min_value, max_value):
        return max(min_value, min(value, max_value))

    @staticmethod
    def debug_value(value):
        if not math.isfinite(value):
            return float("nan")
        return float(round(value, 3))


def main():
    rclpy.init()
    node = ScanSafetyFilterNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
