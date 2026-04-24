from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import os
import xacro


def generate_launch_description():
    use_joint_gui = LaunchConfiguration("use_joint_gui")
    package_share = get_package_share_directory("my_robot_description")
    model_path = os.path.join(package_share, "urdf", "robot.urdf.xacro")
    rviz_config = PathJoinSubstitution(
        [FindPackageShare("my_robot_description"), "rviz", "model.rviz"]
    )

    robot_description = {
        "robot_description": xacro.process_file(model_path).toxml()
    }

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "use_joint_gui",
                default_value="true",
                description="Start joint_state_publisher_gui if true.",
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                parameters=[robot_description],
                output="screen",
            ),
            Node(
                package="joint_state_publisher_gui",
                executable="joint_state_publisher_gui",
                condition=IfCondition(use_joint_gui),
                output="screen",
            ),
            Node(
                package="joint_state_publisher",
                executable="joint_state_publisher",
                condition=UnlessCondition(use_joint_gui),
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
