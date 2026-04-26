import os
import tempfile

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro


def generate_launch_description():
    package_share = get_package_share_directory("my_robot_description")
    model_path = os.path.join(package_share, "urdf", "robot.urdf.xacro")
    gazebo_launch = os.path.join(package_share, "launch", "gazebo_world.launch.py")

    entity_name = LaunchConfiguration("entity_name")
    spawn_x = LaunchConfiguration("spawn_x")
    spawn_y = LaunchConfiguration("spawn_y")
    spawn_z = LaunchConfiguration("spawn_z")
    spawn_yaw = LaunchConfiguration("spawn_yaw")

    robot_description_xml = xacro.process_file(model_path).toxml()

    spawn_urdf_path = os.path.join(
        tempfile.gettempdir(), "my_robot_description_spawn.urdf"
    )
    with open(spawn_urdf_path, "w", encoding="utf-8") as urdf_file:
        urdf_file.write(robot_description_xml)

    return LaunchDescription(
        [
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
                description="Initial z position. Keep it slightly above ground.",
            ),
            DeclareLaunchArgument(
                "spawn_yaw",
                default_value="0.0",
                description="Initial yaw angle in radians.",
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(gazebo_launch),
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                parameters=[
                    {
                        "robot_description": robot_description_xml,
                        "use_sim_time": True,
                    }
                ],
                output="screen",
            ),
            TimerAction(
                period=4.0,
                actions=[
                    Node(
                        package="ros_gz_sim",
                        executable="create",
                        arguments=[
                            "--world",
                            "learning_room",
                            "--file",
                            spawn_urdf_path,
                            "--name",
                            entity_name,
                            "-x",
                            spawn_x,
                            "-y",
                            spawn_y,
                            "-z",
                            spawn_z,
                            "-Y",
                            spawn_yaw,
                        ],
                        output="screen",
                    )
                ],
            ),
        ]
    )
