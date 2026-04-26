from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    record_bag = LaunchConfiguration("record_bag")
    bag_name = LaunchConfiguration("bag_name")
    params_file = LaunchConfiguration("params_file")

    base_launch = PathJoinSubstitution(
        [FindPackageShare("my_robot_description"), "launch", "keyboard_control.launch.py"]
    )
    default_params = PathJoinSubstitution(
        [FindPackageShare("my_robot_description"), "config", "wall_follow.yaml"]
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "record_bag",
                default_value="false",
                description="If true, start rosbag recording from the base launch.",
            ),
            DeclareLaunchArgument(
                "bag_name",
                default_value="wall_follow_session",
                description="rosbag output directory name.",
            ),
            DeclareLaunchArgument(
                "params_file",
                default_value=default_params,
                description="YAML file with wall-follow parameters.",
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(base_launch),
                launch_arguments={
                    "enable_auto_avoid": "false",
                    "record_bag": record_bag,
                    "bag_name": bag_name,
                }.items(),
            ),
            Node(
                package="my_robot_description",
                executable="wall_follow.py",
                parameters=[params_file],
                output="screen",
            ),
        ]
    )
