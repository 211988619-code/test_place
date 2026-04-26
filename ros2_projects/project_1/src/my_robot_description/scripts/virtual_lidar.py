#!/usr/bin/env python3

import math
import random

import rclpy
from geometry_msgs.msg import Point
from nav_msgs.msg import Odometry
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker, MarkerArray


class VirtualLidarNode(Node):
    def __init__(self):
        super().__init__("virtual_lidar")

        self.declare_parameter("publish_rate", 10.0)
        self.declare_parameter("frame_id", "lidar_link")
        self.declare_parameter("range_min", 0.05)
        self.declare_parameter("range_max", 8.0)
        self.declare_parameter("angle_min", -3.14159)
        self.declare_parameter("angle_max", 3.14159)
        self.declare_parameter("angle_increment", 0.0174533)
        self.declare_parameter("noise_std", 0.005)
        self.declare_parameter("lidar_offset_x", 0.125)
        self.declare_parameter("lidar_offset_y", 0.0)
        self.declare_parameter("lidar_yaw_offset", 0.0)
        self.declare_parameter("room_x_min", -4.0)
        self.declare_parameter("room_x_max", 4.0)
        self.declare_parameter("room_y_min", -3.0)
        self.declare_parameter("room_y_max", 3.0)

        self.publish_rate = float(self.get_parameter("publish_rate").value)
        self.frame_id = str(self.get_parameter("frame_id").value)
        self.range_min = float(self.get_parameter("range_min").value)
        self.range_max = float(self.get_parameter("range_max").value)
        self.angle_min = float(self.get_parameter("angle_min").value)
        self.angle_max = float(self.get_parameter("angle_max").value)
        self.angle_increment = float(self.get_parameter("angle_increment").value)
        self.noise_std = float(self.get_parameter("noise_std").value)
        self.lidar_offset_x = float(self.get_parameter("lidar_offset_x").value)
        self.lidar_offset_y = float(self.get_parameter("lidar_offset_y").value)
        self.lidar_yaw_offset = float(self.get_parameter("lidar_yaw_offset").value)
        self.room_x_min = float(self.get_parameter("room_x_min").value)
        self.room_x_max = float(self.get_parameter("room_x_max").value)
        self.room_y_min = float(self.get_parameter("room_y_min").value)
        self.room_y_max = float(self.get_parameter("room_y_max").value)

        self.rect_obstacles = [
            {"cx": 1.2, "cy": 0.8, "sx": 0.8, "sy": 0.5},
            {"cx": -1.4, "cy": -0.6, "sx": 0.7, "sy": 1.0},
            {"cx": 0.2, "cy": -1.7, "sx": 1.0, "sy": 0.4},
        ]
        self.circle_obstacles = [
            {"cx": -0.8, "cy": 1.6, "r": 0.35},
            {"cx": 2.1, "cy": -1.5, "r": 0.3},
        ]

        self.base_x = 0.0
        self.base_y = 0.0
        self.base_yaw = 0.0

        self.odom_subscriber = self.create_subscription(
            Odometry, "/odom", self.odom_callback, 10
        )
        self.scan_publisher = self.create_publisher(LaserScan, "/scan", 10)
        self.scene_publisher = self.create_publisher(MarkerArray, "/scene_markers", 1)
        self.timer = self.create_timer(1.0 / self.publish_rate, self.publish_scan_and_scene)

        self.get_logger().info(
            "virtual_lidar started: "
            f"rate={self.publish_rate:.1f} Hz, "
            f"range=[{self.range_min:.2f}, {self.range_max:.2f}] m, "
            f"angles=[{self.angle_min:.2f}, {self.angle_max:.2f}] rad"
        )

    def odom_callback(self, msg):
        self.base_x = float(msg.pose.pose.position.x)
        self.base_y = float(msg.pose.pose.position.y)
        self.base_yaw = self.quaternion_to_yaw(
            msg.pose.pose.orientation.x,
            msg.pose.pose.orientation.y,
            msg.pose.pose.orientation.z,
            msg.pose.pose.orientation.w,
        )

    def publish_scan_and_scene(self):
        now = self.get_clock().now().to_msg()
        lidar_x, lidar_y, lidar_yaw = self.compute_lidar_pose()

        scan = LaserScan()
        scan.header.stamp = now
        scan.header.frame_id = self.frame_id
        scan.angle_min = self.angle_min
        scan.angle_max = self.angle_max
        scan.angle_increment = self.angle_increment
        scan.time_increment = 0.0
        scan.scan_time = 1.0 / self.publish_rate
        scan.range_min = self.range_min
        scan.range_max = self.range_max
        scan.ranges = self.compute_ranges(lidar_x, lidar_y, lidar_yaw)
        self.scan_publisher.publish(scan)

        scene = self.build_scene_markers(now)
        self.scene_publisher.publish(scene)

    def compute_lidar_pose(self):
        cos_yaw = math.cos(self.base_yaw)
        sin_yaw = math.sin(self.base_yaw)
        lidar_x = self.base_x + cos_yaw * self.lidar_offset_x - sin_yaw * self.lidar_offset_y
        lidar_y = self.base_y + sin_yaw * self.lidar_offset_x + cos_yaw * self.lidar_offset_y
        lidar_yaw = self.base_yaw + self.lidar_yaw_offset
        return lidar_x, lidar_y, lidar_yaw

    def compute_ranges(self, origin_x, origin_y, lidar_yaw):
        ranges = []
        sample_count = int(round((self.angle_max - self.angle_min) / self.angle_increment)) + 1

        for index in range(sample_count):
            ray_angle = lidar_yaw + self.angle_min + index * self.angle_increment
            distance = self.cast_ray(origin_x, origin_y, ray_angle)

            if math.isfinite(distance):
                if self.noise_std > 0.0:
                    distance += random.gauss(0.0, self.noise_std)
                distance = max(self.range_min, min(self.range_max, distance))
                ranges.append(float(distance))
            else:
                ranges.append(float("inf"))

        return ranges

    def cast_ray(self, origin_x, origin_y, ray_angle):
        direction_x = math.cos(ray_angle)
        direction_y = math.sin(ray_angle)
        min_distance = float("inf")

        min_distance = min(
            min_distance,
            self.ray_vertical_intersection(
                origin_x, origin_y, direction_x, direction_y, self.room_x_min, self.room_y_min, self.room_y_max
            ),
        )
        min_distance = min(
            min_distance,
            self.ray_vertical_intersection(
                origin_x, origin_y, direction_x, direction_y, self.room_x_max, self.room_y_min, self.room_y_max
            ),
        )
        min_distance = min(
            min_distance,
            self.ray_horizontal_intersection(
                origin_x, origin_y, direction_x, direction_y, self.room_y_min, self.room_x_min, self.room_x_max
            ),
        )
        min_distance = min(
            min_distance,
            self.ray_horizontal_intersection(
                origin_x, origin_y, direction_x, direction_y, self.room_y_max, self.room_x_min, self.room_x_max
            ),
        )

        for obstacle in self.rect_obstacles:
            half_x = obstacle["sx"] / 2.0
            half_y = obstacle["sy"] / 2.0
            x_min = obstacle["cx"] - half_x
            x_max = obstacle["cx"] + half_x
            y_min = obstacle["cy"] - half_y
            y_max = obstacle["cy"] + half_y

            min_distance = min(
                min_distance,
                self.ray_vertical_intersection(origin_x, origin_y, direction_x, direction_y, x_min, y_min, y_max),
            )
            min_distance = min(
                min_distance,
                self.ray_vertical_intersection(origin_x, origin_y, direction_x, direction_y, x_max, y_min, y_max),
            )
            min_distance = min(
                min_distance,
                self.ray_horizontal_intersection(origin_x, origin_y, direction_x, direction_y, y_min, x_min, x_max),
            )
            min_distance = min(
                min_distance,
                self.ray_horizontal_intersection(origin_x, origin_y, direction_x, direction_y, y_max, x_min, x_max),
            )

        for obstacle in self.circle_obstacles:
            min_distance = min(
                min_distance,
                self.ray_circle_intersection(
                    origin_x,
                    origin_y,
                    direction_x,
                    direction_y,
                    obstacle["cx"],
                    obstacle["cy"],
                    obstacle["r"],
                ),
            )

        if min_distance < self.range_min or min_distance > self.range_max:
            return float("inf")
        return min_distance

    @staticmethod
    def ray_vertical_intersection(origin_x, origin_y, direction_x, direction_y, line_x, y_min, y_max):
        if abs(direction_x) < 1e-9:
            return float("inf")

        distance = (line_x - origin_x) / direction_x
        if distance <= 0.0:
            return float("inf")

        y_hit = origin_y + distance * direction_y
        if y_hit < y_min or y_hit > y_max:
            return float("inf")
        return distance

    @staticmethod
    def ray_horizontal_intersection(origin_x, origin_y, direction_x, direction_y, line_y, x_min, x_max):
        if abs(direction_y) < 1e-9:
            return float("inf")

        distance = (line_y - origin_y) / direction_y
        if distance <= 0.0:
            return float("inf")

        x_hit = origin_x + distance * direction_x
        if x_hit < x_min or x_hit > x_max:
            return float("inf")
        return distance

    @staticmethod
    def ray_circle_intersection(origin_x, origin_y, direction_x, direction_y, center_x, center_y, radius):
        offset_x = origin_x - center_x
        offset_y = origin_y - center_y

        b_term = 2.0 * (direction_x * offset_x + direction_y * offset_y)
        c_term = offset_x * offset_x + offset_y * offset_y - radius * radius
        discriminant = b_term * b_term - 4.0 * c_term
        if discriminant < 0.0:
            return float("inf")

        sqrt_discriminant = math.sqrt(discriminant)
        distance_1 = (-b_term - sqrt_discriminant) / 2.0
        distance_2 = (-b_term + sqrt_discriminant) / 2.0

        candidates = [distance for distance in (distance_1, distance_2) if distance > 0.0]
        if not candidates:
            return float("inf")
        return min(candidates)

    def build_scene_markers(self, stamp):
        markers = MarkerArray()

        room = Marker()
        room.header.frame_id = "odom"
        room.header.stamp = stamp
        room.ns = "scene_room"
        room.id = 0
        room.type = Marker.LINE_STRIP
        room.action = Marker.ADD
        room.scale.x = 0.05
        room.color.r = 0.4
        room.color.g = 0.85
        room.color.b = 0.95
        room.color.a = 1.0
        room.points = [
            self.point(self.room_x_min, self.room_y_min),
            self.point(self.room_x_max, self.room_y_min),
            self.point(self.room_x_max, self.room_y_max),
            self.point(self.room_x_min, self.room_y_max),
            self.point(self.room_x_min, self.room_y_min),
        ]
        markers.markers.append(room)

        marker_id = 1
        for obstacle in self.rect_obstacles:
            marker = Marker()
            marker.header.frame_id = "odom"
            marker.header.stamp = stamp
            marker.ns = "scene_rect"
            marker.id = marker_id
            marker_id += 1
            marker.type = Marker.CUBE
            marker.action = Marker.ADD
            marker.pose.position.x = obstacle["cx"]
            marker.pose.position.y = obstacle["cy"]
            marker.pose.position.z = 0.2
            marker.pose.orientation.w = 1.0
            marker.scale.x = obstacle["sx"]
            marker.scale.y = obstacle["sy"]
            marker.scale.z = 0.4
            marker.color.r = 0.9
            marker.color.g = 0.6
            marker.color.b = 0.2
            marker.color.a = 0.9
            markers.markers.append(marker)

        for obstacle in self.circle_obstacles:
            marker = Marker()
            marker.header.frame_id = "odom"
            marker.header.stamp = stamp
            marker.ns = "scene_circle"
            marker.id = marker_id
            marker_id += 1
            marker.type = Marker.CYLINDER
            marker.action = Marker.ADD
            marker.pose.position.x = obstacle["cx"]
            marker.pose.position.y = obstacle["cy"]
            marker.pose.position.z = 0.2
            marker.pose.orientation.w = 1.0
            marker.scale.x = 2.0 * obstacle["r"]
            marker.scale.y = 2.0 * obstacle["r"]
            marker.scale.z = 0.4
            marker.color.r = 0.25
            marker.color.g = 0.7
            marker.color.b = 0.3
            marker.color.a = 0.9
            markers.markers.append(marker)

        return markers

    @staticmethod
    def point(x_value, y_value):
        point = Point()
        point.x = float(x_value)
        point.y = float(y_value)
        point.z = 0.02
        return point

    @staticmethod
    def quaternion_to_yaw(x_value, y_value, z_value, w_value):
        siny_cosp = 2.0 * (w_value * z_value + x_value * y_value)
        cosy_cosp = 1.0 - 2.0 * (y_value * y_value + z_value * z_value)
        return math.atan2(siny_cosp, cosy_cosp)


def main():
    rclpy.init()
    node = VirtualLidarNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
