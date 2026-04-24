#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from geometry_msgs.msg import TransformStamped
# 注意：TF 广播器在这里导入
from tf2_ros import TransformBroadcaster

class TFFusionNode(Node):
    def __init__(self):
        super().__init__('tf_fusion_node')
        
        # 1. 创建一个 TF 广播器（大喇叭，用来告诉 RViz 机器人在哪）
        self.tf_broadcaster = TransformBroadcaster(self)

        # 2. 用来暂存最新数据的“草稿纸”
        self.latest_x = 0.0
        self.latest_y = 0.0
        self.latest_qz = 0.0
        self.latest_qw = 1.0

        # 3. 订阅里程计（只关心 X 和 Y）
        self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        # 4. 订阅 IMU（只关心四元数朝向）
        self.create_subscription(Imu, '/imu/data', self.imu_callback, 10)

        self.get_logger().info('TF 融合节点已启动！正在拼接位置与朝向...')

    def odom_callback(self, msg):
        # 收到里程计数据：更新 X 和 Y
        self.latest_x = msg.pose.pose.position.x
        self.latest_y = msg.pose.pose.position.y
        # 然后立刻广播一次最新的 TF
        self.broadcast_tf()

    def imu_callback(self, msg):
        # 收到 IMU 数据：更新朝向（四元数）
        self.latest_qz = msg.orientation.z
        self.latest_qw = msg.orientation.w
        # 然后立刻广播一次最新的 TF
        self.broadcast_tf()

    def broadcast_tf(self):
        # 核心！构建 TF 消息
        t = TransformStamped()
        
        # 时间戳必须是现在的瞬间
        t.header.stamp = self.get_clock().now().to_msg()
        
        # 父坐标系是 "odom"（世界地图）
        t.header.frame_id = 'odom'
        # 子坐标系是 "base_link"（机器人的肚脐眼）
        t.child_frame_id = 'base_link'
        
        # 填入从里程计拿来的位置
        t.transform.translation.x = self.latest_x
        t.transform.translation.y = self.latest_y
        t.transform.translation.z = 0.0
        
        # 填入从 IMU 拿来的朝向
        t.transform.rotation.z = self.latest_qz
        t.transform.rotation.w = self.latest_qw
        
        # 发射！🎯
        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = TFFusionNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
