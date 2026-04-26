// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_description:msg/WallFollowDebug.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "my_robot_description/msg/wall_follow_debug.hpp"


#ifndef MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__BUILDER_HPP_
#define MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_description/msg/detail/wall_follow_debug__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_description
{

namespace msg
{

namespace builder
{

class Init_WallFollowDebug_in_acquire_mode
{
public:
  explicit Init_WallFollowDebug_in_acquire_mode(::my_robot_description::msg::WallFollowDebug & msg)
  : msg_(msg)
  {}
  ::my_robot_description::msg::WallFollowDebug in_acquire_mode(::my_robot_description::msg::WallFollowDebug::_in_acquire_mode_type arg)
  {
    msg_.in_acquire_mode = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

class Init_WallFollowDebug_wall_lost
{
public:
  explicit Init_WallFollowDebug_wall_lost(::my_robot_description::msg::WallFollowDebug & msg)
  : msg_(msg)
  {}
  Init_WallFollowDebug_in_acquire_mode wall_lost(::my_robot_description::msg::WallFollowDebug::_wall_lost_type arg)
  {
    msg_.wall_lost = std::move(arg);
    return Init_WallFollowDebug_in_acquire_mode(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

class Init_WallFollowDebug_front_blocked
{
public:
  explicit Init_WallFollowDebug_front_blocked(::my_robot_description::msg::WallFollowDebug & msg)
  : msg_(msg)
  {}
  Init_WallFollowDebug_wall_lost front_blocked(::my_robot_description::msg::WallFollowDebug::_front_blocked_type arg)
  {
    msg_.front_blocked = std::move(arg);
    return Init_WallFollowDebug_wall_lost(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

class Init_WallFollowDebug_angular_command
{
public:
  explicit Init_WallFollowDebug_angular_command(::my_robot_description::msg::WallFollowDebug & msg)
  : msg_(msg)
  {}
  Init_WallFollowDebug_front_blocked angular_command(::my_robot_description::msg::WallFollowDebug::_angular_command_type arg)
  {
    msg_.angular_command = std::move(arg);
    return Init_WallFollowDebug_front_blocked(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

class Init_WallFollowDebug_linear_command
{
public:
  explicit Init_WallFollowDebug_linear_command(::my_robot_description::msg::WallFollowDebug & msg)
  : msg_(msg)
  {}
  Init_WallFollowDebug_angular_command linear_command(::my_robot_description::msg::WallFollowDebug::_linear_command_type arg)
  {
    msg_.linear_command = std::move(arg);
    return Init_WallFollowDebug_angular_command(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

class Init_WallFollowDebug_front_speed_scale
{
public:
  explicit Init_WallFollowDebug_front_speed_scale(::my_robot_description::msg::WallFollowDebug & msg)
  : msg_(msg)
  {}
  Init_WallFollowDebug_linear_command front_speed_scale(::my_robot_description::msg::WallFollowDebug::_front_speed_scale_type arg)
  {
    msg_.front_speed_scale = std::move(arg);
    return Init_WallFollowDebug_linear_command(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

class Init_WallFollowDebug_wall_angle_error
{
public:
  explicit Init_WallFollowDebug_wall_angle_error(::my_robot_description::msg::WallFollowDebug & msg)
  : msg_(msg)
  {}
  Init_WallFollowDebug_front_speed_scale wall_angle_error(::my_robot_description::msg::WallFollowDebug::_wall_angle_error_type arg)
  {
    msg_.wall_angle_error = std::move(arg);
    return Init_WallFollowDebug_front_speed_scale(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

class Init_WallFollowDebug_distance_error
{
public:
  explicit Init_WallFollowDebug_distance_error(::my_robot_description::msg::WallFollowDebug & msg)
  : msg_(msg)
  {}
  Init_WallFollowDebug_wall_angle_error distance_error(::my_robot_description::msg::WallFollowDebug::_distance_error_type arg)
  {
    msg_.distance_error = std::move(arg);
    return Init_WallFollowDebug_wall_angle_error(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

class Init_WallFollowDebug_diagonal_range
{
public:
  explicit Init_WallFollowDebug_diagonal_range(::my_robot_description::msg::WallFollowDebug & msg)
  : msg_(msg)
  {}
  Init_WallFollowDebug_distance_error diagonal_range(::my_robot_description::msg::WallFollowDebug::_diagonal_range_type arg)
  {
    msg_.diagonal_range = std::move(arg);
    return Init_WallFollowDebug_distance_error(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

class Init_WallFollowDebug_side_range
{
public:
  explicit Init_WallFollowDebug_side_range(::my_robot_description::msg::WallFollowDebug & msg)
  : msg_(msg)
  {}
  Init_WallFollowDebug_diagonal_range side_range(::my_robot_description::msg::WallFollowDebug::_side_range_type arg)
  {
    msg_.side_range = std::move(arg);
    return Init_WallFollowDebug_diagonal_range(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

class Init_WallFollowDebug_front_range
{
public:
  explicit Init_WallFollowDebug_front_range(::my_robot_description::msg::WallFollowDebug & msg)
  : msg_(msg)
  {}
  Init_WallFollowDebug_side_range front_range(::my_robot_description::msg::WallFollowDebug::_front_range_type arg)
  {
    msg_.front_range = std::move(arg);
    return Init_WallFollowDebug_side_range(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

class Init_WallFollowDebug_state
{
public:
  explicit Init_WallFollowDebug_state(::my_robot_description::msg::WallFollowDebug & msg)
  : msg_(msg)
  {}
  Init_WallFollowDebug_front_range state(::my_robot_description::msg::WallFollowDebug::_state_type arg)
  {
    msg_.state = std::move(arg);
    return Init_WallFollowDebug_front_range(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

class Init_WallFollowDebug_stamp
{
public:
  Init_WallFollowDebug_stamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WallFollowDebug_state stamp(::my_robot_description::msg::WallFollowDebug::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_WallFollowDebug_state(msg_);
  }

private:
  ::my_robot_description::msg::WallFollowDebug msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_description::msg::WallFollowDebug>()
{
  return my_robot_description::msg::builder::Init_WallFollowDebug_stamp();
}

}  // namespace my_robot_description

#endif  // MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__BUILDER_HPP_
