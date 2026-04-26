import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ros_gz_bridge.actions import RosGzBridge


def generate_launch_description():
    package_share = get_package_share_directory("my_robot_description")
    spawn_launch = os.path.join(package_share, "launch", "spawn_robot_in_room.launch.py")
    bridge_config = os.path.join(package_share, "config", "gazebo_bridge.yaml")
    record_bag = LaunchConfiguration("record_bag")
    bag_name = LaunchConfiguration("bag_name")
    entity_name = LaunchConfiguration("entity_name")
    spawn_x = LaunchConfiguration("spawn_x")
    spawn_y = LaunchConfiguration("spawn_y")
    spawn_z = LaunchConfiguration("spawn_z")
    spawn_yaw = LaunchConfiguration("spawn_yaw")

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "record_bag",
                default_value="false",
                description="If true, start rosbag recording for Gazebo mode.",
            ),
            DeclareLaunchArgument(
                "bag_name",
                default_value="gazebo_session",
                description="Output bag name or directory passed to ros2 bag record -o.",
            ),
            DeclareLaunchArgument(
                "entity_name",
                default_value="indoor_patrol_bot",
                description="Model name shown inside Gazebo.",
            ),
            DeclareLaunchArgument(
                "spawn_x",
                default_value="0.0",
                description="Initial x position in the room frame.",
            ),
            DeclareLaunchArgument(
                "spawn_y",
                default_value="0.0",
                description="Initial y position in the room frame.",
            ),
            DeclareLaunchArgument(
                "spawn_z",
                default_value="0.20",
                description="Initial z position above the floor.",
            ),
            DeclareLaunchArgument(
                "spawn_yaw",
                default_value="0.0",
                description="Initial yaw angle in radians.",
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(spawn_launch),
                launch_arguments={
                    "entity_name": entity_name,
                    "spawn_x": spawn_x,
                    "spawn_y": spawn_y,
                    "spawn_z": spawn_z,
                    "spawn_yaw": spawn_yaw,
                }.items(),
            ),
            RosGzBridge(
                bridge_name="gazebo_bridge",
                config_file=bridge_config,
            ),
            Node(
                package="ros_gz_image",
                executable="image_bridge",
                arguments=["/camera/image_raw"],
                parameters=[
                    {
                        "qos": "sensor_data",
                        "lazy": True,
                        "subscription_heartbeat": 500,
                    }
                ],
                output="screen",
            ),
            Node(
                package="my_robot_description",
                executable="scan_safety_filter.py",
                parameters=[
                    {
                        "input_topic": "/cmd_vel_input",
                        "output_topic": "/cmd_vel",
                        "enable_safety_stop": True,
                        "enable_safety_slowdown": True,
                        "enable_auto_avoid": False,
                        "front_body_offset": 0.13,
                        "rear_body_offset": 0.38,
                        "safety_stop_distance": 0.18,
                        "safety_slow_distance": 0.80,
                        "safety_angle": 0.45,
                    }
                ],
                output="screen",
            ),
            Node(
                package="my_robot_description",
                executable="odom_to_tf.py",
                parameters=[
                    {
                        "use_sim_time": True,
                        "odom_topic": "/odom",
                        "parent_frame": "odom",
                        "child_frame": "base_footprint",
                    }
                ],
                output="screen",
            ),
            ExecuteProcess(
                cmd=[
                    "ros2",
                    "bag",
                    "record",
                    "-o",
                    bag_name,
                    "/clock",
                    "/cmd_vel",
                    "/cmd_vel_input",
                    "/odom",
                    "/joint_states",
                    "/scan",
                    "/camera/camera_info",
                    "/tf",
                    "/tf_static",
                    "/wall_follow_debug",
                    "/wall_follow_markers",
                ],
                condition=IfCondition(record_bag),
                output="screen",
            ),
        ]
    )
