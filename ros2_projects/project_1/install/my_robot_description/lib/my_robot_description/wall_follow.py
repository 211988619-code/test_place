#!/usr/bin/env python3

import math

import rclpy
from geometry_msgs.msg import Point, Twist
from my_robot_description.msg import WallFollowDebug
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker, MarkerArray


class WallFollowNode(Node):
    def __init__(self):
        super().__init__("wall_follow")

        self.declare_parameter("publish_rate", 10.0)
        self.declare_parameter("follow_side", "left")
        self.declare_parameter("target_distance", 0.60)
        self.declare_parameter("acquire_distance", 1.20)
        self.declare_parameter("forward_speed", 0.25)
        self.declare_parameter("search_turn_speed", 0.45)
        self.declare_parameter("acquire_turn_speed", 0.18)
        self.declare_parameter("max_turn_speed", 1.00)
        self.declare_parameter("front_stop_distance", 0.55)
        self.declare_parameter("front_slow_distance", 0.90)
        self.declare_parameter("lost_wall_distance", 1.60)
        self.declare_parameter("front_sector_half_angle", 0.30)
        self.declare_parameter("side_sector_half_angle", 0.20)
        self.declare_parameter("kp_distance", 2.0)
        self.declare_parameter("kp_angle", 1.2)
        self.declare_parameter("debug_topic", "/wall_follow_debug")
        self.declare_parameter("debug_marker_topic", "/wall_follow_markers")
        self.declare_parameter("publish_debug_markers", True)

        self.publish_rate = float(self.get_parameter("publish_rate").value)
        self.follow_side = str(self.get_parameter("follow_side").value).lower()
        self.target_distance = float(self.get_parameter("target_distance").value)
        self.acquire_distance = float(self.get_parameter("acquire_distance").value)
        self.forward_speed = float(self.get_parameter("forward_speed").value)
        self.search_turn_speed = float(self.get_parameter("search_turn_speed").value)
        self.acquire_turn_speed = float(
            self.get_parameter("acquire_turn_speed").value
        )
        self.max_turn_speed = float(self.get_parameter("max_turn_speed").value)
        self.front_stop_distance = float(
            self.get_parameter("front_stop_distance").value
        )
        self.front_slow_distance = float(
            self.get_parameter("front_slow_distance").value
        )
        self.lost_wall_distance = float(
            self.get_parameter("lost_wall_distance").value
        )
        self.front_sector_half_angle = float(
            self.get_parameter("front_sector_half_angle").value
        )
        self.side_sector_half_angle = float(
            self.get_parameter("side_sector_half_angle").value
        )
        self.kp_distance = float(self.get_parameter("kp_distance").value)
        self.kp_angle = float(self.get_parameter("kp_angle").value)
        self.debug_topic = str(self.get_parameter("debug_topic").value)
        self.debug_marker_topic = str(
            self.get_parameter("debug_marker_topic").value
        )
        self.publish_debug_markers = bool(
            self.get_parameter("publish_debug_markers").value
        )

        if self.follow_side not in ("left", "right"):
            self.get_logger().warn(
                "Invalid follow_side '%s', fallback to 'left'" % self.follow_side
            )
            self.follow_side = "left"

        self.latest_scan = None
        self.last_state = ""

        self.scan_subscription = self.create_subscription(
            LaserScan, "/scan", self.scan_callback, 10
        )
        self.cmd_publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        self.debug_publisher = self.create_publisher(
            WallFollowDebug, self.debug_topic, 10
        )
        self.marker_publisher = self.create_publisher(
            MarkerArray, self.debug_marker_topic, 10
        )
        self.timer = self.create_timer(1.0 / self.publish_rate, self.control_loop)

        self.get_logger().info(
            "wall_follow started: "
            f"follow_side={self.follow_side}, "
            f"target_distance={self.target_distance:.2f} m, "
            f"acquire_distance={self.acquire_distance:.2f} m, "
            f"forward_speed={self.forward_speed:.2f} m/s, "
            f"max_turn_speed={self.max_turn_speed:.2f} rad/s, "
            f"debug_topic={self.debug_topic}"
        )

    def scan_callback(self, msg):
        self.latest_scan = msg

    def control_loop(self):
        if self.latest_scan is None:
            self.publish_cmd(0.0, 0.0)
            self.log_state_once("waiting_for_scan")
            self.publish_debug(
                stamp=self.get_clock().now().to_msg(),
                state="waiting_for_scan",
                front_range=float("nan"),
                side_range=float("nan"),
                diagonal_range=float("nan"),
                distance_error=float("nan"),
                wall_angle_error=float("nan"),
                front_speed_scale=0.0,
                linear_command=0.0,
                angular_command=0.0,
                front_blocked=False,
                wall_lost=True,
                in_acquire_mode=False,
            )
            self.clear_markers(self.get_clock().now().to_msg())
            return

        wall_sign = 1.0 if self.follow_side == "left" else -1.0
        side_center = wall_sign * (math.pi / 2.0)
        diagonal_center = wall_sign * (math.pi / 4.0)

        front_observation = self.get_sector_observation(
            self.latest_scan, 0.0, self.front_sector_half_angle
        )
        side_observation = self.get_sector_observation(
            self.latest_scan, side_center, self.side_sector_half_angle
        )
        diagonal_observation = self.get_sector_observation(
            self.latest_scan, diagonal_center, self.side_sector_half_angle
        )
        front_range = front_observation["range"]
        side_range = side_observation["range"]
        diagonal_range = diagonal_observation["range"]
        front_blocked = (
            math.isfinite(front_range) and front_range < self.front_stop_distance
        )
        wall_lost = (not math.isfinite(side_range)) or (
            side_range > self.lost_wall_distance
        )
        in_acquire_mode = math.isfinite(side_range) and (
            self.acquire_distance < side_range <= self.lost_wall_distance
        )
        state = "following_wall"
        front_speed_scale = self.compute_front_speed_scale(front_range)
        distance_error = float("nan")
        wall_angle_error = float("nan")
        linear = 0.0
        angular = 0.0

        if front_blocked:
            if not math.isfinite(side_range) or side_range > self.target_distance:
                angular = wall_sign * self.max_turn_speed
                state = "front_blocked_turn_toward_wall"
            else:
                angular = -wall_sign * self.max_turn_speed
                state = "front_blocked_turn_away_from_wall"
        elif wall_lost:
            linear = 0.8 * self.forward_speed
            angular = wall_sign * self.search_turn_speed
            state = "searching_wall"
        elif in_acquire_mode:
            linear = self.forward_speed
            angular = wall_sign * self.acquire_turn_speed
            if (
                math.isfinite(diagonal_range)
                and diagonal_range < side_range
                and diagonal_range < self.acquire_distance
            ):
                angular = 0.5 * wall_sign * self.acquire_turn_speed
            state = "approaching_wall"
        else:
            distance_error = self.target_distance - side_range
            wall_angle_error = 0.0
            if math.isfinite(diagonal_range):
                wall_angle_error = diagonal_range - side_range

            angular = (
                -wall_sign * self.kp_distance * distance_error
                + wall_sign * self.kp_angle * wall_angle_error
            )
            angular = self.clamp(angular, -self.max_turn_speed, self.max_turn_speed)

            turn_scale = self.clamp(
                1.0 - 0.35 * abs(angular) / max(self.max_turn_speed, 1e-6), 0.55, 1.0
            )
            linear = self.forward_speed * min(front_speed_scale, turn_scale)
            state = "following_wall"

        self.log_state_once(state)
        self.publish_cmd(linear, angular)
        self.publish_debug(
            stamp=self.latest_scan.header.stamp,
            state=state,
            front_range=front_range,
            side_range=side_range,
            diagonal_range=diagonal_range,
            distance_error=distance_error,
            wall_angle_error=wall_angle_error,
            front_speed_scale=front_speed_scale,
            linear_command=linear,
            angular_command=angular,
            front_blocked=front_blocked,
            wall_lost=wall_lost,
            in_acquire_mode=in_acquire_mode,
        )
        if self.publish_debug_markers:
            self.publish_markers(
                self.latest_scan.header,
                state,
                front_observation,
                side_observation,
                diagonal_observation,
                side_center,
            )

    def compute_front_speed_scale(self, front_range):
        if not math.isfinite(front_range):
            return 1.0
        if front_range <= self.front_stop_distance:
            return 0.0
        if front_range >= self.front_slow_distance:
            return 1.0

        span = self.front_slow_distance - self.front_stop_distance
        ratio = (front_range - self.front_stop_distance) / max(span, 1e-6)
        return self.clamp(ratio, 0.25, 1.0)

    def get_sector_observation(self, scan, center_angle, half_width):
        min_range = float("inf")
        min_angle = center_angle

        for index, range_value in enumerate(scan.ranges):
            if not math.isfinite(range_value):
                continue
            if not (scan.range_min <= range_value <= scan.range_max):
                continue

            angle = scan.angle_min + index * scan.angle_increment
            if abs(self.normalize_angle(angle - center_angle)) > half_width:
                continue

            if range_value < min_range:
                min_range = range_value
                min_angle = angle

        return {"range": min_range, "angle": min_angle}

    def publish_cmd(self, linear, angular):
        msg = Twist()
        msg.linear.x = float(linear)
        msg.angular.z = float(angular)
        self.cmd_publisher.publish(msg)

    def publish_debug(
        self,
        stamp,
        state,
        front_range,
        side_range,
        diagonal_range,
        distance_error,
        wall_angle_error,
        front_speed_scale,
        linear_command,
        angular_command,
        front_blocked,
        wall_lost,
        in_acquire_mode,
    ):
        msg = WallFollowDebug()
        msg.stamp = stamp
        msg.state = state
        msg.front_range = self.debug_value(front_range)
        msg.side_range = self.debug_value(side_range)
        msg.diagonal_range = self.debug_value(diagonal_range)
        msg.distance_error = self.debug_value(distance_error)
        msg.wall_angle_error = self.debug_value(wall_angle_error)
        msg.front_speed_scale = self.debug_value(front_speed_scale)
        msg.linear_command = self.debug_value(linear_command)
        msg.angular_command = self.debug_value(angular_command)
        msg.front_blocked = front_blocked
        msg.wall_lost = wall_lost
        msg.in_acquire_mode = in_acquire_mode
        self.debug_publisher.publish(msg)

    def publish_markers(
        self,
        header,
        state,
        front_observation,
        side_observation,
        diagonal_observation,
        side_center,
    ):
        markers = MarkerArray()
        markers.markers.append(self.make_delete_all_marker(header))
        markers.markers.append(
            self.make_ray_marker(
                header,
                marker_id=0,
                namespace="wall_follow_front",
                observation=front_observation,
                fallback_length=self.front_slow_distance,
                color=(1.0, 0.25, 0.25, 0.95),
            )
        )
        markers.markers.append(
            self.make_ray_marker(
                header,
                marker_id=1,
                namespace="wall_follow_side",
                observation=side_observation,
                fallback_length=max(self.target_distance, 0.3),
                color=(0.2, 0.6, 1.0, 0.95),
            )
        )
        markers.markers.append(
            self.make_ray_marker(
                header,
                marker_id=2,
                namespace="wall_follow_diagonal",
                observation=diagonal_observation,
                fallback_length=max(self.acquire_distance, 0.4),
                color=(0.2, 0.95, 0.4, 0.95),
            )
        )
        markers.markers.append(
            self.make_target_marker(
                header, marker_id=3, side_center=side_center, target_distance=self.target_distance
            )
        )
        markers.markers.append(
            self.make_text_marker(header, marker_id=4, text=state)
        )
        self.marker_publisher.publish(markers)

    def clear_markers(self, stamp):
        if not self.publish_debug_markers:
            return
        markers = MarkerArray()
        markers.markers.append(self.make_delete_all_marker_from_stamp(stamp))
        self.marker_publisher.publish(markers)

    def make_delete_all_marker(self, header):
        marker = Marker()
        marker.header = header
        marker.action = Marker.DELETEALL
        return marker

    def make_delete_all_marker_from_stamp(self, stamp):
        marker = Marker()
        marker.header.stamp = stamp
        marker.header.frame_id = "lidar_link"
        marker.action = Marker.DELETEALL
        return marker

    def make_ray_marker(
        self, header, marker_id, namespace, observation, fallback_length, color
    ):
        marker = Marker()
        marker.header = header
        marker.ns = namespace
        marker.id = marker_id
        marker.type = Marker.ARROW
        marker.action = Marker.ADD
        marker.scale.x = 0.03
        marker.scale.y = 0.06
        marker.scale.z = 0.08
        marker.color.r = color[0]
        marker.color.g = color[1]
        marker.color.b = color[2]
        marker.color.a = color[3]
        marker.points = [
            Point(x=0.0, y=0.0, z=0.02),
            self.point_from_polar(
                observation["angle"],
                observation["range"],
                fallback_length,
                z=0.02,
            ),
        ]
        return marker

    def make_target_marker(self, header, marker_id, side_center, target_distance):
        marker = Marker()
        marker.header = header
        marker.ns = "wall_follow_target"
        marker.id = marker_id
        marker.type = Marker.ARROW
        marker.action = Marker.ADD
        marker.scale.x = 0.02
        marker.scale.y = 0.04
        marker.scale.z = 0.05
        marker.color.r = 1.0
        marker.color.g = 0.95
        marker.color.b = 0.25
        marker.color.a = 0.85
        marker.points = [
            Point(x=0.0, y=0.0, z=0.01),
            self.point_from_polar(side_center, target_distance, target_distance, z=0.01),
        ]
        return marker

    def make_text_marker(self, header, marker_id, text):
        marker = Marker()
        marker.header = header
        marker.ns = "wall_follow_state"
        marker.id = marker_id
        marker.type = Marker.TEXT_VIEW_FACING
        marker.action = Marker.ADD
        marker.pose.position.x = 0.0
        marker.pose.position.y = 0.0
        marker.pose.position.z = 0.35
        marker.pose.orientation.w = 1.0
        marker.scale.z = 0.12
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 1.0
        marker.color.a = 0.95
        marker.text = text
        return marker

    def log_state_once(self, state):
        if state == self.last_state:
            return
        self.last_state = state
        self.get_logger().info(f"wall_follow state: {state}")

    @staticmethod
    def clamp(value, min_value, max_value):
        return max(min_value, min(value, max_value))

    @staticmethod
    def debug_value(value):
        if not math.isfinite(value):
            return float("nan")
        return float(round(value, 3))

    @staticmethod
    def point_from_polar(angle, measured_range, fallback_length, z):
        length = measured_range if math.isfinite(measured_range) else fallback_length
        return Point(
            x=float(length * math.cos(angle)),
            y=float(length * math.sin(angle)),
            z=float(z),
        )

    @staticmethod
    def normalize_angle(angle):
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi:
            angle += 2.0 * math.pi
        return angle


def main():
    rclpy.init()
    node = WallFollowNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.publish_cmd(0.0, 0.0)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
