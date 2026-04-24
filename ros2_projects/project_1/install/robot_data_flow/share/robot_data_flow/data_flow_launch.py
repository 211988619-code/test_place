#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 虚拟 IMU
        Node(
            package='robot_data_flow',
            executable='fake_imu_node.py',
            name='fake_imu_node',
            output='screen'
        ),
        # 虚拟里程计
        Node(
            package='robot_data_flow',
            executable='fake_odom_node.py',
            name='fake_odom_node',
            output='screen'
        ),
        # TF 融合大脑
        Node(
            package='robot_data_flow',
            executable='tf_fusion_node.py',
            name='tf_fusion_node',
            output='screen'
        ),
    ])
