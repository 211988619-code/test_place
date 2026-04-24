from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. 启动小海龟仿真器节点
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim'
        ),
        
        # 2. 启动你写的画圆节点
        Node(
            package='turtle_auto',
            executable='auto_circle',
            name='auto_circle'
        ),
    ])
