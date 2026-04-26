#!/usr/bin/env python3

import math

import rclpy
from geometry_msgs.msg import PoseWithCovarianceStamped
from rclpy.node import Node


class AutoInitialPoseNode(Node):
    def __init__(self):
        super().__init__("auto_initial_pose")

        self.declare_parameter("topic", "/initialpose")
        self.declare_parameter("frame_id", "map")
        self.declare_parameter("pose_x", 0.0)
        self.declare_parameter("pose_y", 0.0)
        self.declare_parameter("pose_yaw", 0.0)
        self.declare_parameter("publish_count", 5)
        self.declare_parameter("publish_period", 0.5)
        self.declare_parameter("position_covariance", 0.25)
        self.declare_parameter("yaw_covariance", 0.20)

        topic = str(self.get_parameter("topic").value)
        self.frame_id = str(self.get_parameter("frame_id").value)
        self.pose_x = float(self.get_parameter("pose_x").value)
        self.pose_y = float(self.get_parameter("pose_y").value)
        self.pose_yaw = float(self.get_parameter("pose_yaw").value)
        self.publish_count = max(1, int(self.get_parameter("publish_count").value))
        publish_period = float(self.get_parameter("publish_period").value)
        self.position_covariance = float(
            self.get_parameter("position_covariance").value
        )
        self.yaw_covariance = float(self.get_parameter("yaw_covariance").value)
        self.published = 0

        self.publisher = self.create_publisher(PoseWithCovarianceStamped, topic, 10)
        self.timer = self.create_timer(publish_period, self.publish_initial_pose)

        self.get_logger().info(
            "auto_initial_pose started: "
            f"topic={topic}, frame_id={self.frame_id}, "
            f"pose=({self.pose_x:.2f}, {self.pose_y:.2f}, {self.pose_yaw:.2f})"
        )

    def publish_initial_pose(self):
        msg = PoseWithCovarianceStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = self.frame_id
        msg.pose.pose.position.x = self.pose_x
        msg.pose.pose.position.y = self.pose_y
        msg.pose.pose.position.z = 0.0
        msg.pose.pose.orientation.z = math.sin(self.pose_yaw / 2.0)
        msg.pose.pose.orientation.w = math.cos(self.pose_yaw / 2.0)
        msg.pose.covariance[0] = self.position_covariance
        msg.pose.covariance[7] = self.position_covariance
        msg.pose.covariance[35] = self.yaw_covariance
        self.publisher.publish(msg)

        self.published += 1
        self.get_logger().info(
            "Published /initialpose "
            f"{self.published}/{self.publish_count}: "
            f"x={self.pose_x:.2f}, y={self.pose_y:.2f}, yaw={self.pose_yaw:.2f}"
        )

        if self.published >= self.publish_count:
            self.timer.cancel()
            self.get_logger().info("auto_initial_pose finished publishing.")


def main():
    rclpy.init()
    node = AutoInitialPoseNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
