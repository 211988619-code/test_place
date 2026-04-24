cmake_minimum_required(VERSION 3.8)
project(my_robot_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY launch rviz urdf
  DESTINATION share/${PROJECT_NAME}
)

install(
  PROGRAMS
    scripts/wheel_demo.py
    scripts/diff_drive_demo.py
    scripts/cmd_vel_drive.py
    scripts/keyboard_teleop.py
    scripts/virtual_lidar.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
