#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState


class WheelDemoNode(Node):
    def __init__(self):
        super().__init__("wheel_demo")

        self.declare_parameter("wheel_speed", 1.2)
        self.declare_parameter("publish_rate", 30.0)

        self.wheel_speed = float(self.get_parameter("wheel_speed").value)
        self.publish_rate = float(self.get_parameter("publish_rate").value)

        self.publisher = self.create_publisher(JointState, "/joint_states", 10)
        self.timer = self.create_timer(1.0 / self.publish_rate, self.publish_joint_states)

        self.left_position = 0.0
        self.right_position = 0.0
        self.last_time = self.get_clock().now()

        self.get_logger().info(
            f"wheel_demo started: wheel_speed={self.wheel_speed:.2f} rad/s, "
            f"publish_rate={self.publish_rate:.1f} Hz"
        )

    def publish_joint_states(self):
        now = self.get_clock().now()
        dt = (now - self.last_time).nanoseconds / 1e9
        self.last_time = now

        self.left_position += self.wheel_speed * dt
        self.right_position += self.wheel_speed * dt

        msg = JointState()
        msg.header.stamp = now.to_msg()
        msg.name = ["left_wheel_joint", "right_wheel_joint"]
        msg.position = [self.left_position, self.right_position]
        msg.velocity = [self.wheel_speed, self.wheel_speed]

        self.publisher.publish(msg)


def main():
    rclpy.init()
    node = WheelDemoNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
