#!/usr/bin/env python3

import copy

import rclpy
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy, HistoryPolicy, QoSProfile, ReliabilityPolicy
from rosgraph_msgs.msg import Clock
from sensor_msgs.msg import LaserScan


class ScanToSlamNode(Node):
    def __init__(self):
        super().__init__("scan_to_slam")

        self.declare_parameter("input_topic", "/scan")
        self.declare_parameter("output_topic", "/scan_slam")
        self.declare_parameter("restamp_to_now", False)
        self.declare_parameter("clock_topic", "/clock")

        input_topic = str(self.get_parameter("input_topic").value)
        output_topic = str(self.get_parameter("output_topic").value)
        self.restamp_to_now = bool(self.get_parameter("restamp_to_now").value)
        clock_topic = str(self.get_parameter("clock_topic").value)

        input_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=10,
        )
        output_qos = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=20,
        )
        clock_qos = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=10,
        )

        self.subscription = self.create_subscription(
            LaserScan, input_topic, self.scan_callback, input_qos
        )
        self.publisher = self.create_publisher(LaserScan, output_topic, output_qos)
        self.clock_subscription = self.create_subscription(
            Clock, clock_topic, self.clock_callback, clock_qos
        )
        self.latest_clock = None
        self.warned_no_clock = False
        self.forwarded_first_scan = False

        self.get_logger().info(
            "scan_to_slam started: "
            f"input_topic={input_topic}, output_topic={output_topic}, "
            f"clock_topic={clock_topic}, restamp_to_now={self.restamp_to_now}"
        )

    def clock_callback(self, msg):
        self.latest_clock = msg.clock
        self.warned_no_clock = False

    def scan_callback(self, msg):
        if self.restamp_to_now and self.latest_clock is None:
            if not self.warned_no_clock:
                self.get_logger().warn(
                    "No /clock received yet, skipping scan forwarding until sim time is available"
                )
                self.warned_no_clock = True
            return

        outgoing = copy.deepcopy(msg)
        if self.restamp_to_now:
            outgoing.header.stamp = self.latest_clock
        self.publisher.publish(outgoing)
        if not self.forwarded_first_scan:
            self.forwarded_first_scan = True
            self.get_logger().info(
                "Forwarded first scan for SLAM: "
                f"stamp={outgoing.header.stamp.sec}.{outgoing.header.stamp.nanosec:09d}, "
                f"frame_id={outgoing.header.frame_id}"
            )


def main():
    rclpy.init()
    node = ScanToSlamNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
