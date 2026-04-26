#!/usr/bin/env python3

import select
import sys
import termios
import tty
import time

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


HELP_TEXT = """
Keyboard teleop for /cmd_vel
----------------------------
w: forward
x: backward
a: turn left
d: turn right
s: stop
q: faster linear speed
z: slower linear speed
e: faster angular speed
c: slower angular speed
Ctrl-C: quit
"""


class KeyboardTeleopNode(Node):
    def __init__(self):
        super().__init__("keyboard_teleop")

        self.declare_parameter("publish_rate", 10.0)
        self.declare_parameter("linear_step", 0.05)
        self.declare_parameter("angular_step", 0.2)
        self.declare_parameter("max_linear_speed", 0.8)
        self.declare_parameter("max_angular_speed", 1.5)
        self.declare_parameter("key_timeout", 1.5)
        self.declare_parameter("idle_auto_stop", True)
        self.declare_parameter("angular_hold_timeout", 0.25)

        self.publish_rate = float(self.get_parameter("publish_rate").value)
        self.linear_step = float(self.get_parameter("linear_step").value)
        self.angular_step = float(self.get_parameter("angular_step").value)
        self.max_linear_speed = float(self.get_parameter("max_linear_speed").value)
        self.max_angular_speed = float(self.get_parameter("max_angular_speed").value)
        self.key_timeout = float(self.get_parameter("key_timeout").value)
        self.idle_auto_stop = bool(self.get_parameter("idle_auto_stop").value)
        self.angular_hold_timeout = float(
            self.get_parameter("angular_hold_timeout").value
        )

        self.linear_speed = 0.0
        self.angular_speed = 0.0
        self.last_key_time = time.monotonic()
        self.last_turn_key_time = time.monotonic()

        self.publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        self.timer = self.create_timer(1.0 / self.publish_rate, self.publish_cmd_vel)

        self.get_logger().info(HELP_TEXT)
        self.get_logger().info(
            "idle_auto_stop=%s, key_timeout=%.2f s, angular_hold_timeout=%.2f s"
            % (self.idle_auto_stop, self.key_timeout, self.angular_hold_timeout)
        )
        self.print_status()

    def handle_key(self, key):
        if key == "w":
            self.linear_speed = min(
                self.linear_speed + self.linear_step, self.max_linear_speed
            )
        elif key == "x":
            self.linear_speed = max(
                self.linear_speed - self.linear_step, -self.max_linear_speed
            )
        elif key == "a":
            self.angular_speed = min(
                self.angular_speed + self.angular_step, self.max_angular_speed
            )
            self.last_turn_key_time = time.monotonic()
        elif key == "d":
            self.angular_speed = max(
                self.angular_speed - self.angular_step, -self.max_angular_speed
            )
            self.last_turn_key_time = time.monotonic()
        elif key == "s":
            self.linear_speed = 0.0
            self.angular_speed = 0.0
            self.last_turn_key_time = time.monotonic()
        elif key == "q":
            self.linear_step *= 1.2
        elif key == "z":
            self.linear_step = max(0.01, self.linear_step / 1.2)
        elif key == "e":
            self.angular_step *= 1.2
        elif key == "c":
            self.angular_step = max(0.05, self.angular_step / 1.2)
        else:
            return

        self.last_key_time = time.monotonic()
        self.print_status()

    def publish_cmd_vel(self):
        turn_timed_out = (
            time.monotonic() - self.last_turn_key_time > self.angular_hold_timeout
        )
        if turn_timed_out and self.angular_speed != 0.0:
            self.angular_speed = 0.0
            self.print_status()

        if (
            self.idle_auto_stop
            and
            time.monotonic() - self.last_key_time > self.key_timeout
            and (self.linear_speed != 0.0 or self.angular_speed != 0.0)
        ):
            self.linear_speed = 0.0
            self.angular_speed = 0.0
            self.print_status()

        msg = Twist()
        msg.linear.x = self.linear_speed
        msg.angular.z = self.angular_speed
        self.publisher.publish(msg)

    def print_status(self):
        self.get_logger().info(
            "cmd_vel status: "
            f"linear={self.linear_speed:.2f} m/s, "
            f"angular={self.angular_speed:.2f} rad/s, "
            f"linear_step={self.linear_step:.2f}, "
            f"angular_step={self.angular_step:.2f}"
        )

    def stop_robot(self):
        self.linear_speed = 0.0
        self.angular_speed = 0.0
        self.publish_cmd_vel()
        self.print_status()


def read_key(timeout):
    tty.setraw(sys.stdin.fileno())
    readable, _, _ = select.select([sys.stdin], [], [], timeout)
    if readable:
        return sys.stdin.read(1)
    return ""


def main():
    settings = termios.tcgetattr(sys.stdin)
    rclpy.init()
    node = KeyboardTeleopNode()

    try:
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.0)
            key = read_key(0.1)
            if key == "\x03":
                break
            if key:
                node.handle_key(key)
    except KeyboardInterrupt:
        pass
    finally:
        node.stop_robot()
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
