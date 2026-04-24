#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class FakeImuNode(Node):
    def __init__(self):
        super().__init__('fake_imu_node')
        self.publisher_ = self.create_publisher(Imu, '/imu/data', 10)
        self.timer = self.create_timer(0.02, self.publish_imu) # 50Hz发送
        self.start_time = self.get_clock().now().seconds_nanoseconds()[0]
        self.get_logger().info('虚拟 IMU 已启动！')

    def publish_imu(self):
        msg = Imu()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'imu_link'

        # 计算当前时间，每 6.28 秒转一圈（2π）
        current_time = self.get_clock().now().seconds_nanoseconds()[0] - self.start_time
        yaw = (current_time * 0.5) % (2 * math.pi) 

        # 填入角速度 (绕 Z 轴转，所以是 z = 0.5 rad/s)
        msg.angular_velocity.z = 0.5 
        # 填入四元数朝向 (这里用简单的公式把 yaw 转成四元数，ROS 必须用四元数)
        msg.orientation.x = 0.0
        msg.orientation.y = 0.0
        msg.orientation.z = math.sin(yaw / 2)
        msg.orientation.w = math.cos(yaw / 2)

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = FakeImuNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
