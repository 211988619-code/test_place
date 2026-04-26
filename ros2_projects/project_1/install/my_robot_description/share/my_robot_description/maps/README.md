# Maps

Use this directory for saved slam_toolbox map artifacts.

Recommended outputs:

- `learning_room_map`
  - occupancy-grid map saved through `/slam_toolbox/save_map`
  - produces files such as `learning_room_map.pgm` and `learning_room_map.yaml`
- `learning_room_posegraph`
  - serialized pose-graph saved through `/slam_toolbox/serialize_map`
  - used by `gazebo_localization.launch.py`

Important:

- If you use normal `colcon build`, runtime-generated map files in `src/my_robot_description/maps`
  are not copied into `install/share/.../maps`.
- The localization launch therefore defaults to the source-package `maps/` directory, not the
  installed package-share `maps/` directory.
- In `gazebo_localization.launch.py`, `spawn_x/y/yaw` control where the robot appears in Gazebo,
  while `initial_pose_x/y/yaw` control the `/initialpose` estimate sent to localization.
