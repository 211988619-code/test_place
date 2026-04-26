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
    params_file = LaunchConfiguration("params_file")
    record_bag = LaunchConfiguration("record_bag")
    bag_name = LaunchConfiguration("bag_name")

    default_params = os.path.join(
        package_share, "config", "wall_follow_gazebo.yaml"
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "params_file",
                default_value=default_params,
                description="YAML file with Gazebo wall-follow parameters.",
            ),
            DeclareLaunchArgument(
                "record_bag",
                default_value="false",
                description="If true, start rosbag recording for Gazebo wall-follow mode.",
            ),
            DeclareLaunchArgument(
                "bag_name",
                default_value="gazebo_wall_follow_session",
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
                package="my_robot_description",
                executable="wall_follow.py",
                parameters=[params_file],
                remappings=[("/cmd_vel", "/cmd_vel_input")],
                output="screen",
            ),
        ]
    )
