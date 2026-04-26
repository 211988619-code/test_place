from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition
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

    publish_rate = LaunchConfiguration("publish_rate")
    cmd_timeout = LaunchConfiguration("cmd_timeout")
    max_linear_speed = LaunchConfiguration("max_linear_speed")
    max_angular_speed = LaunchConfiguration("max_angular_speed")
    max_linear_accel = LaunchConfiguration("max_linear_accel")
    max_angular_accel = LaunchConfiguration("max_angular_accel")
    enable_safety_stop = LaunchConfiguration("enable_safety_stop")
    enable_safety_slowdown = LaunchConfiguration("enable_safety_slowdown")
    safety_stop_distance = LaunchConfiguration("safety_stop_distance")
    safety_slow_distance = LaunchConfiguration("safety_slow_distance")
    safety_angle = LaunchConfiguration("safety_angle")
    enable_auto_avoid = LaunchConfiguration("enable_auto_avoid")
    auto_avoid_max_turn_speed = LaunchConfiguration("auto_avoid_max_turn_speed")
    auto_avoid_gain = LaunchConfiguration("auto_avoid_gain")
    front_body_offset = LaunchConfiguration("front_body_offset")
    rear_body_offset = LaunchConfiguration("rear_body_offset")
    enable_virtual_lidar = LaunchConfiguration("enable_virtual_lidar")
    lidar_publish_rate = LaunchConfiguration("lidar_publish_rate")
    record_bag = LaunchConfiguration("record_bag")
    bag_name = LaunchConfiguration("bag_name")

    robot_description = {
        "robot_description": xacro.process_file(model_path).toxml()
    }

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "publish_rate",
                default_value="30.0",
                description="Drive node state publish rate in Hz.",
            ),
            DeclareLaunchArgument(
                "cmd_timeout",
                default_value="0.5",
                description="Seconds before missing /cmd_vel commands force a stop.",
            ),
            DeclareLaunchArgument(
                "max_linear_speed",
                default_value="0.8",
                description="Drive-node clamp for linear speed in m/s.",
            ),
            DeclareLaunchArgument(
                "max_angular_speed",
                default_value="1.5",
                description="Drive-node clamp for angular speed in rad/s.",
            ),
            DeclareLaunchArgument(
                "max_linear_accel",
                default_value="1.0",
                description="Drive-node linear acceleration limit in m/s^2.",
            ),
            DeclareLaunchArgument(
                "max_angular_accel",
                default_value="2.5",
                description="Drive-node angular acceleration limit in rad/s^2.",
            ),
            DeclareLaunchArgument(
                "enable_safety_stop",
                default_value="true",
                description="If true, block forward motion when an obstacle is too close.",
            ),
            DeclareLaunchArgument(
                "enable_safety_slowdown",
                default_value="true",
                description="If true, slow down as obstacles enter the safety sector.",
            ),
            DeclareLaunchArgument(
                "safety_stop_distance",
                default_value="0.18",
                description="Minimum allowed hull-to-obstacle clearance in meters.",
            ),
            DeclareLaunchArgument(
                "safety_slow_distance",
                default_value="0.80",
                description="Hull-to-obstacle clearance at which speed reduction begins.",
            ),
            DeclareLaunchArgument(
                "safety_angle",
                default_value="0.45",
                description="Half-angle of the front safety sector in radians.",
            ),
            DeclareLaunchArgument(
                "enable_auto_avoid",
                default_value="true",
                description="If true, auto-turn when forward motion is blocked by an obstacle.",
            ),
            DeclareLaunchArgument(
                "auto_avoid_max_turn_speed",
                default_value="0.9",
                description="Maximum angular speed used by auto avoidance in rad/s.",
            ),
            DeclareLaunchArgument(
                "auto_avoid_gain",
                default_value="2.0",
                description="Proportional gain from left/right clearance difference to turn rate.",
            ),
            DeclareLaunchArgument(
                "front_body_offset",
                default_value="0.13",
                description="Distance from lidar to front hull in meters.",
            ),
            DeclareLaunchArgument(
                "rear_body_offset",
                default_value="0.38",
                description="Distance from lidar to rear hull in meters.",
            ),
            DeclareLaunchArgument(
                "enable_virtual_lidar",
                default_value="true",
                description="If true, start the virtual 2D lidar node.",
            ),
            DeclareLaunchArgument(
                "lidar_publish_rate",
                default_value="10.0",
                description="Virtual lidar publish rate in Hz.",
            ),
            DeclareLaunchArgument(
                "record_bag",
                default_value="false",
                description="If true, start rosbag recording for core robot topics.",
            ),
            DeclareLaunchArgument(
                "bag_name",
                default_value="keyboard_session",
                description="Output bag name or directory passed to 'ros2 bag record -o'.",
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                parameters=[robot_description],
                output="screen",
            ),
            Node(
                package="my_robot_description",
                executable="cmd_vel_drive.py",
                parameters=[
                    {
                        "publish_rate": publish_rate,
                        "cmd_timeout": cmd_timeout,
                        "max_linear_speed": max_linear_speed,
                        "max_angular_speed": max_angular_speed,
                        "max_linear_accel": max_linear_accel,
                        "max_angular_accel": max_angular_accel,
                        "enable_safety_stop": enable_safety_stop,
                        "enable_safety_slowdown": enable_safety_slowdown,
                        "safety_stop_distance": safety_stop_distance,
                        "safety_slow_distance": safety_slow_distance,
                        "safety_angle": safety_angle,
                        "enable_auto_avoid": enable_auto_avoid,
                        "auto_avoid_max_turn_speed": auto_avoid_max_turn_speed,
                        "auto_avoid_gain": auto_avoid_gain,
                        "front_body_offset": front_body_offset,
                        "rear_body_offset": rear_body_offset,
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
            Node(
                package="my_robot_description",
                executable="virtual_lidar.py",
                condition=IfCondition(enable_virtual_lidar),
                parameters=[
                    {
                        "publish_rate": lidar_publish_rate,
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
                    "/cmd_vel",
                    "/odom",
                    "/joint_states",
                    "/tf",
                    "/tf_static",
                    "/scan",
                    "/scene_markers",
                    "/safety_debug",
                    "/wall_follow_debug",
                    "/wall_follow_markers",
                ],
                condition=IfCondition(record_bag),
                output="screen",
            ),
        ]
    )
