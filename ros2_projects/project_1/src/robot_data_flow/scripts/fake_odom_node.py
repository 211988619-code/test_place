#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class FakeOdomNode(Node):
    def __init__(self):
        super().__init__('fake_odom_node')
        self.publisher_ = self.create_publisher(Odometry, '/odom', 10)
        self.timer = self.create_timer(0.02, self.publish_odom) # 50Hz
        self.start_time = self.get_clock().now().seconds_nanoseconds()[0]
        self.get_logger().info('虚拟里程计已启动！')

    def publish_odom(self):
        msg = Odometry()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'odom'
        msg.child_frame_id = 'base_link'

        current_time = self.get_clock().now().seconds_nanoseconds()[0] - self.start_time
        
        # 算圆的坐标：半径 R=2, 角速度 w=0.5
        R = 2.0
        w = 0.5
        x = R * math.sin(w * current_time)
        y = R - R * math.cos(w * current_time)

        # 填入位置
        msg.pose.pose.position.x = x
        msg.pose.pose.position.y = y
        msg.pose.pose.position.z = 0.0

        # 填入线速度 (圆周运动线速度 v = w * R = 1.0)
        msg.twist.twist.linear.x = w * R

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = FakeOdomNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
