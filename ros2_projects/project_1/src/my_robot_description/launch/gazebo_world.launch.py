from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    world = LaunchConfiguration("world")

    default_world = PathJoinSubstitution(
        [FindPackageShare("my_robot_description"), "worlds", "learning_room.sdf"]
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "world",
                default_value=default_world,
                description="Absolute path to the Gazebo world file to load.",
            ),
            ExecuteProcess(
                cmd=["gz", "sim", "-r", world],
                output="screen",
            ),
        ]
    )
