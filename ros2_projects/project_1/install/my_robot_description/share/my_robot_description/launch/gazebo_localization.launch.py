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
    workspace_root = os.path.abspath(
        os.path.join(package_share, "..", "..", "..", "..")
    )
    gazebo_drive_launch = os.path.join(
        package_share, "launch", "gazebo_drive.launch.py"
    )
    default_localization_config = os.path.join(
        package_share, "config", "slam_localization_gazebo.yaml"
    )
    default_rviz_config = os.path.join(
        package_share, "rviz", "localization.rviz"
    )
    default_pose_graph = os.path.join(
        workspace_root,
        "src",
        "my_robot_description",
        "maps",
        "learning_room_posegraph",
    )

    localization_params_file = LaunchConfiguration("localization_params_file")
    rviz_config = LaunchConfiguration("rviz_config")
    pose_graph_file = LaunchConfiguration("pose_graph_file")
    spawn_x = LaunchConfiguration("spawn_x")
    spawn_y = LaunchConfiguration("spawn_y")
    spawn_z = LaunchConfiguration("spawn_z")
    spawn_yaw = LaunchConfiguration("spawn_yaw")
    initial_pose_x = LaunchConfiguration("initial_pose_x")
    initial_pose_y = LaunchConfiguration("initial_pose_y")
    initial_pose_yaw = LaunchConfiguration("initial_pose_yaw")
    publish_initial_pose = LaunchConfiguration("publish_initial_pose")
    initial_pose_delay = LaunchConfiguration("initial_pose_delay")
    localization_params_with_subst = ParameterFile(
        localization_params_file,
        allow_substs=True,
    )

    localization_node = LifecycleNode(
        package="slam_toolbox",
        executable="localization_slam_toolbox_node",
        name="slam_toolbox",
        namespace="",
        parameters=[
            localization_params_with_subst,
            {
                "use_sim_time": True,
                "use_lifecycle_manager": False,
                "map_file_name": pose_graph_file,
            },
        ],
        output="screen",
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "localization_params_file",
                default_value=default_localization_config,
                description="YAML file with slam_toolbox localization parameters.",
            ),
            DeclareLaunchArgument(
                "rviz_config",
                default_value=default_rviz_config,
                description="RViz config used for localization mode.",
            ),
            DeclareLaunchArgument(
                "pose_graph_file",
                default_value=default_pose_graph,
                description="Serialized slam_toolbox pose-graph path without extension.",
            ),
            DeclareLaunchArgument(
                "spawn_x",
                default_value="0.0",
                description="Initial Gazebo x position, also reused as default localization x.",
            ),
            DeclareLaunchArgument(
                "spawn_y",
                default_value="0.0",
                description="Initial Gazebo y position, also reused as default localization y.",
            ),
            DeclareLaunchArgument(
                "spawn_z",
                default_value="0.20",
                description="Initial Gazebo z position.",
            ),
            DeclareLaunchArgument(
                "spawn_yaw",
                default_value="0.0",
                description="Initial Gazebo yaw, also reused as default localization yaw.",
            ),
            DeclareLaunchArgument(
                "publish_initial_pose",
                default_value="true",
                description="If true, publish /initialpose automatically after localization starts.",
            ),
            DeclareLaunchArgument(
                "initial_pose_x",
                default_value=spawn_x,
                description="Initial localization x in the loaded map frame.",
            ),
            DeclareLaunchArgument(
                "initial_pose_y",
                default_value=spawn_y,
                description="Initial localization y in the loaded map frame.",
            ),
            DeclareLaunchArgument(
                "initial_pose_yaw",
                default_value=spawn_yaw,
                description="Initial localization yaw in the loaded map frame.",
            ),
            DeclareLaunchArgument(
                "initial_pose_delay",
                default_value="9.0",
                description="Delay before the helper node publishes /initialpose.",
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(gazebo_drive_launch),
                launch_arguments={
                    "record_bag": "false",
                    "spawn_x": spawn_x,
                    "spawn_y": spawn_y,
                    "spawn_z": spawn_z,
                    "spawn_yaw": spawn_yaw,
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
                    localization_node,
                ],
            ),
            TimerAction(
                period=7.5,
                actions=[
                    LogInfo(
                        msg="[LifecycleLaunch] slam_toolbox localization is configuring."
                    ),
                    ExecuteProcess(
                        cmd=["ros2", "lifecycle", "set", "/slam_toolbox", "configure"],
                        output="screen",
                    ),
                ],
            ),
            TimerAction(
                period=10.5,
                actions=[
                    LogInfo(
                        msg="[LifecycleLaunch] slam_toolbox localization is activating."
                    ),
                    ExecuteProcess(
                        cmd=["ros2", "lifecycle", "set", "/slam_toolbox", "activate"],
                        output="screen",
                    ),
                ],
            ),
            TimerAction(
                period=initial_pose_delay,
                actions=[
                    Node(
                        package="my_robot_description",
                        executable="auto_initial_pose.py",
                        parameters=[
                            {
                                "use_sim_time": True,
                                "pose_x": initial_pose_x,
                                "pose_y": initial_pose_y,
                                "pose_yaw": initial_pose_yaw,
                                "frame_id": "map",
                                "publish_count": 5,
                                "publish_period": 0.5,
                                "position_covariance": 0.25,
                                "yaw_covariance": 0.20,
                            }
                        ],
                        condition=IfCondition(publish_initial_pose),
                        output="screen",
                    )
                ],
            ),
        ]
    )
