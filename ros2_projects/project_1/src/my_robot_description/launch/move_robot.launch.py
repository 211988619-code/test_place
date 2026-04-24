from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import os
import xacro


def generate_launch_description():
    package_share = get_package_share_directory("my_robot_description")
    model_path = os.path.join(package_share, "urdf", "robot.urdf.xacro")
    rviz_config = PathJoinSubstitution(
        [FindPackageShare("my_robot_description"), "rviz", "motion.rviz"]
    )

    linear_speed = LaunchConfiguration("linear_speed")
    angular_speed = LaunchConfiguration("angular_speed")
    publish_rate = LaunchConfiguration("publish_rate")

    robot_description = {
        "robot_description": xacro.process_file(model_path).toxml()
    }

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "linear_speed",
                default_value="0.25",
                description="Robot forward speed in m/s.",
            ),
            DeclareLaunchArgument(
                "angular_speed",
                default_value="0.0",
                description="Robot yaw rate in rad/s.",
            ),
            DeclareLaunchArgument(
                "publish_rate",
                default_value="30.0",
                description="State publish rate in Hz.",
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                parameters=[robot_description],
                output="screen",
            ),
            Node(
                package="my_robot_description",
                executable="diff_drive_demo.py",
                parameters=[
                    {
                        "linear_speed": linear_speed,
                        "angular_speed": angular_speed,
                        "publish_rate": publish_rate,
                    }
                ],
                output="screen",
            ),
            Node(
                package="rviz2",
                executable="rviz2",
                arguments=["-d", rviz_config],
                output="screen",
            ),
        ]
    )
