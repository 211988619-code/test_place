import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package_share = get_package_share_directory("my_robot_description")
    gazebo_drive_launch = os.path.join(
        package_share, "launch", "gazebo_drive.launch.py"
    )
    rviz_config = os.path.join(package_share, "rviz", "motion.rviz")
    record_bag = LaunchConfiguration("record_bag")
    bag_name = LaunchConfiguration("bag_name")

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "record_bag",
                default_value="false",
                description="If true, start rosbag recording for Gazebo + RViz mode.",
            ),
            DeclareLaunchArgument(
                "bag_name",
                default_value="gazebo_rviz_session",
                description="rosbag output directory name.",
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(gazebo_drive_launch),
                launch_arguments={
                    "record_bag": record_bag,
                    "bag_name": bag_name,
                }.items(),
            ),
            Node(
                package="rviz2",
                executable="rviz2",
                arguments=["-d", rviz_config],
                parameters=[{"use_sim_time": True}],
                output="screen",
            ),
        ]
    )
