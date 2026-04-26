cmake_minimum_required(VERSION 3.8)
project(my_robot_description)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(builtin_interfaces REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/SafetyDebug.msg"
  "msg/WallFollowDebug.msg"
  DEPENDENCIES builtin_interfaces
)

install(
  DIRECTORY launch rviz urdf worlds config maps
  DESTINATION share/${PROJECT_NAME}
)

install(
  PROGRAMS
    scripts/wheel_demo.py
    scripts/diff_drive_demo.py
    scripts/cmd_vel_drive.py
    scripts/keyboard_teleop.py
    scripts/odom_to_tf.py
    scripts/odom_to_joint_states.py
    scripts/scan_to_slam.py
    scripts/save_slam_artifacts.py
    scripts/auto_initial_pose.py
    scripts/scan_safety_filter.py
    scripts/virtual_lidar.py
    scripts/wall_follow.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
