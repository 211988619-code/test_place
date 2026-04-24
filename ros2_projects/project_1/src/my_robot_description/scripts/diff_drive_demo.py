#!/usr/bin/env python3

import math

import rclpy
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry
from rclpy.node import Node
from sensor_msgs.msg import JointState
from tf2_ros import TransformBroadcaster


class DiffDriveDemoNode(Node):
    def __init__(self):
        super().__init__("diff_drive_demo")

        self.declare_parameter("linear_speed", 0.25)
        self.declare_parameter("angular_speed", 0.0)
        self.declare_parameter("publish_rate", 30.0)
        self.declare_parameter("wheel_radius", 0.08)
        self.declare_parameter("wheel_separation", 0.38)

        self.linear_speed = float(self.get_parameter("linear_speed").value)
        self.angular_speed = float(self.get_parameter("angular_speed").value)
        self.publish_rate = float(self.get_parameter("publish_rate").value)
        self.wheel_radius = float(self.get_parameter("wheel_radius").value)
        self.wheel_separation = float(self.get_parameter("wheel_separation").value)

        self.joint_publisher = self.create_publisher(JointState, "/joint_states", 10)
        self.odom_publisher = self.create_publisher(Odometry, "/odom", 10)
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(1.0 / self.publish_rate, self.publish_state)

        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.left_wheel_position = 0.0
        self.right_wheel_position = 0.0
        self.last_time = self.get_clock().now()

        self.get_logger().info(
            "diff_drive_demo started: "
            f"linear_speed={self.linear_speed:.2f} m/s, "
            f"angular_speed={self.angular_speed:.2f} rad/s, "
            f"publish_rate={self.publish_rate:.1f} Hz"
        )

    def publish_state(self):
        now = self.get_clock().now()
        dt = (now - self.last_time).nanoseconds / 1e9
        self.last_time = now

        if dt <= 0.0:
            return

        self.x += self.linear_speed * math.cos(self.yaw) * dt
        self.y += self.linear_speed * math.sin(self.yaw) * dt
        self.yaw += self.angular_speed * dt

        left_wheel_velocity = (
            self.linear_speed - self.angular_speed * self.wheel_separation / 2.0
        ) / self.wheel_radius
        right_wheel_velocity = (
            self.linear_speed + self.angular_speed * self.wheel_separation / 2.0
        ) / self.wheel_radius

        self.left_wheel_position += left_wheel_velocity * dt
        self.right_wheel_position += right_wheel_velocity * dt

        self.publish_joint_states(now, left_wheel_velocity, right_wheel_velocity)
        self.publish_odom(now)
        self.publish_transform(now)

    def publish_joint_states(self, now, left_wheel_velocity, right_wheel_velocity):
        msg = JointState()
        msg.header.stamp = now.to_msg()
        msg.name = ["left_wheel_joint", "right_wheel_joint"]
        msg.position = [self.left_wheel_position, self.right_wheel_position]
        msg.velocity = [left_wheel_velocity, right_wheel_velocity]
        self.joint_publisher.publish(msg)

    def publish_odom(self, now):
        msg = Odometry()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = "odom"
        msg.child_frame_id = "base_footprint"
        msg.pose.pose.position.x = self.x
        msg.pose.pose.position.y = self.y
        msg.pose.pose.position.z = 0.0

        qz = math.sin(self.yaw / 2.0)
        qw = math.cos(self.yaw / 2.0)
        msg.pose.pose.orientation.z = qz
        msg.pose.pose.orientation.w = qw
        msg.twist.twist.linear.x = self.linear_speed
        msg.twist.twist.angular.z = self.angular_speed
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


def main():
    rclpy.init()
    node = DiffDriveDemoNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
