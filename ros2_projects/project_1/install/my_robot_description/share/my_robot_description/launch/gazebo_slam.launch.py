import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription, LogInfo, TimerAction
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import LifecycleNode, Node
from launch_ros.descriptions import ParameterFile


def generate_launch_description():
    package_share = get_package_share_directory("my_robot_description")
    gazebo_drive_launch = os.path.join(
        package_share, "launch", "gazebo_drive.launch.py"
    )
    default_slam_config = os.path.join(
        package_share, "config", "slam_toolbox_gazebo.yaml"
    )
    default_rviz_config = os.path.join(package_share, "rviz", "slam.rviz")

    slam_params_file = LaunchConfiguration("slam_params_file")
    rviz_config = LaunchConfiguration("rviz_config")
    record_bag = LaunchConfiguration("record_bag")
    bag_name = LaunchConfiguration("bag_name")
    slam_params_file_with_subst = ParameterFile(
        slam_params_file,
        allow_substs=True,
    )

    slam_toolbox_node = LifecycleNode(
        package="slam_toolbox",
        executable="sync_slam_toolbox_node",
        name="slam_toolbox",
        namespace="",
        parameters=[
            slam_params_file_with_subst,
            {
                "use_sim_time": True,
                "use_lifecycle_manager": False,
            },
        ],
        output="screen",
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "slam_params_file",
                default_value=default_slam_config,
                description="YAML file with slam_toolbox parameters.",
            ),
            DeclareLaunchArgument(
                "rviz_config",
                default_value=default_rviz_config,
                description="RViz config used for SLAM mode.",
            ),
            DeclareLaunchArgument(
                "record_bag",
                default_value="false",
                description="If true, start rosbag recording for Gazebo SLAM mode.",
            ),
            DeclareLaunchArgument(
                "bag_name",
                default_value="gazebo_slam_session",
                description="rosbag output directory name.",
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(gazebo_drive_launch),
                launch_arguments={
                    "record_bag": "false",
                }.items(),
            ),
            Node(
                package="my_robot_description",
                executable="scan_to_slam.py",
                parameters=[
                    {
                        "use_sim_time": True,
                        "input_topic": "/scan",
                        "output_topic": "/scan_slam",
                        "restamp_to_now": False,
                    }
                ],
                output="screen",
            ),
            Node(
                package="rviz2",
                executable="rviz2",
                arguments=["-d", rviz_config],
                parameters=[{"use_sim_time": True}],
                output="screen",
            ),
            TimerAction(
                period=6.0,
                actions=[
                    slam_toolbox_node,
                ],
            ),
            TimerAction(
                period=7.5,
                actions=[
                    LogInfo(msg="[LifecycleLaunch] slam_toolbox is configuring."),
                    ExecuteProcess(
                        cmd=["ros2", "lifecycle", "set", "/slam_toolbox", "configure"],
                        output="screen",
                    ),
                ],
            ),
            TimerAction(
                period=9.0,
                actions=[
                    LogInfo(msg="[LifecycleLaunch] slam_toolbox is activating."),
                    ExecuteProcess(
                        cmd=["ros2", "lifecycle", "set", "/slam_toolbox", "activate"],
                        output="screen",
                    ),
                ],
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
                    "/odom",
                    "/scan",
                    "/camera/camera_info",
                    "/tf",
                    "/tf_static",
                    "/map",
                    "/map_metadata",
                ],
                condition=IfCondition(record_bag),
                output="screen",
            ),
        ]
    )
