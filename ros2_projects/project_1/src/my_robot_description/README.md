# my_robot_description

用于学习 URDF、TF、`/cmd_vel` 控制、虚拟 2D 激光雷达和基础避障控制的最小 ROS 2 工程。

## 当前能力

- 机器人模型：`base_footprint`、`base_link`、左右驱动轮、万向轮、`lidar_link`、`camera_link`
- 键盘控制：`keyboard_teleop.py` 发布 `/cmd_vel`
- 底盘驱动：`cmd_vel_drive.py` 订阅 `/cmd_vel`，发布 `/joint_states`、`/odom` 和 TF
- 虚拟雷达：`virtual_lidar.py` 发布 `/scan` 和 `/scene_markers`
- 安全控制：
  - 前进看前方扇区
  - 倒车看后方扇区
  - 先减速，再停车
  - 前方受阻时平滑自动转向绕障
- 可选 rosbag 录制：一键录关键话题

## 运行

```bash
cd ~/ws/urdf_ws
colcon build --packages-select my_robot_description
source install/setup.bash
```

终端 1：

```bash
ros2 launch my_robot_description keyboard_control.launch.py
```

终端 2：

```bash
ros2 run my_robot_description keyboard_teleop.py
```

## 键盘说明

- `w` 前进
- `x` 后退
- `a` 左转
- `d` 右转
- `s` 停车
- `q/z` 增大/减小线速度步长
- `e/c` 增大/减小角速度步长

默认转向键采用“短时保持”逻辑：

- `a/d` 产生角速度
- 松开后如果一小段时间内没有继续按转向键，角速度自动回到 0
- 线速度保持不变，因此小车会恢复直行

## 重要参数

```bash
ros2 launch my_robot_description keyboard_control.launch.py \
  max_linear_speed:=0.8 \
  max_angular_speed:=1.5 \
  max_linear_accel:=1.0 \
  max_angular_accel:=2.5 \
  enable_safety_stop:=true \
  enable_safety_slowdown:=true \
  safety_stop_distance:=0.18 \
  safety_slow_distance:=0.80 \
  safety_angle:=0.45 \
  enable_auto_avoid:=true \
  auto_avoid_max_turn_speed:=0.9 \
  auto_avoid_gain:=2.0 \
  front_body_offset:=0.13 \
  rear_body_offset:=0.38 \
  enable_virtual_lidar:=true \
  lidar_publish_rate:=10.0
```

参数含义：

- `safety_stop_distance`：车体外壳到障碍物的最小允许余量
- `safety_slow_distance`：车体外壳到障碍物的减速起始余量
- `safety_angle`：前方/后方扇区半角
- `front_body_offset`：雷达到车头外壳的距离
- `rear_body_offset`：雷达到车尾外壳的距离
- `auto_avoid_max_turn_speed`：自动绕障最大角速度
- `auto_avoid_gain`：左右前方空间差映射到角速度的比例增益

## 调试建议

如果你感觉“离墙太远就停”，优先检查：

- `safety_stop_distance`
- `front_body_offset`
- `rear_body_offset`

如果你感觉“自动转向太生硬”，优先调整：

- `auto_avoid_max_turn_speed`
- `auto_avoid_gain`
- `safety_angle`

## Service：重置里程计

```bash
ros2 service call /reset_odometry std_srvs/srv/Trigger
```

## rosbag

启动时一起录制：

```bash
ros2 launch my_robot_description keyboard_control.launch.py \
  record_bag:=true \
  bag_name:=session_01
```

单独录制：

```bash
ros2 bag record -o session_01 \
  /cmd_vel /odom /joint_states /tf /tf_static /scan /scene_markers
```
