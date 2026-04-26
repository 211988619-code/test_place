#!/usr/bin/env python3

import math

import rclpy
from nav_msgs.msg import Odometry
from rclpy.node import Node
from sensor_msgs.msg import JointState


class OdomToJointStatesNode(Node):
    def __init__(self):
        super().__init__("odom_to_joint_states")

        self.declare_parameter("odom_topic", "/odom")
        self.declare_parameter("joint_topic", "/joint_states")
        self.declare_parameter("wheel_radius", 0.08)
        self.declare_parameter("wheel_separation", 0.38)

        odom_topic = str(self.get_parameter("odom_topic").value)
        joint_topic = str(self.get_parameter("joint_topic").value)
        self.wheel_radius = float(self.get_parameter("wheel_radius").value)
        self.wheel_separation = float(self.get_parameter("wheel_separation").value)

        self.left_position = 0.0
        self.right_position = 0.0
        self.last_stamp = None

        self.publisher = self.create_publisher(JointState, joint_topic, 10)
        self.subscription = self.create_subscription(
            Odometry, odom_topic, self.odom_callback, 10
        )

        self.get_logger().info(
            "odom_to_joint_states started: "
            f"odom_topic={odom_topic}, joint_topic={joint_topic}, "
            f"wheel_radius={self.wheel_radius:.2f}, "
            f"wheel_separation={self.wheel_separation:.2f}"
        )

    def odom_callback(self, msg):
        current_stamp = msg.header.stamp
        linear = float(msg.twist.twist.linear.x)
        angular = float(msg.twist.twist.angular.z)

        left_velocity = (
            linear - angular * self.wheel_separation / 2.0
        ) / self.wheel_radius
        right_velocity = (
            linear + angular * self.wheel_separation / 2.0
        ) / self.wheel_radius

        if self.last_stamp is not None:
            dt = self.compute_dt_seconds(self.last_stamp, current_stamp)
            if dt > 0.0:
                self.left_position += left_velocity * dt
                self.right_position += right_velocity * dt

        self.last_stamp = current_stamp

        joint_state = JointState()
        joint_state.header.stamp = current_stamp
        joint_state.name = ["left_wheel_joint", "right_wheel_joint"]
        joint_state.position = [self.left_position, self.right_position]
        joint_state.velocity = [left_velocity, right_velocity]
        self.publisher.publish(joint_state)

    @staticmethod
    def compute_dt_seconds(previous_stamp, current_stamp):
        previous = previous_stamp.sec + previous_stamp.nanosec / 1e9
        current = current_stamp.sec + current_stamp.nanosec / 1e9
        return max(0.0, current - previous)


def main():
    rclpy.init()
    node = OdomToJointStatesNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
