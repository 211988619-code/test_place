// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_description:msg/SafetyDebug.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "my_robot_description/msg/safety_debug.hpp"


#ifndef MY_ROBOT_DESCRIPTION__MSG__DETAIL__SAFETY_DEBUG__BUILDER_HPP_
#define MY_ROBOT_DESCRIPTION__MSG__DETAIL__SAFETY_DEBUG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_description/msg/detail/safety_debug__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_description
{

namespace msg
{

namespace builder
{

class Init_SafetyDebug_obstacle_blocked
{
public:
  explicit Init_SafetyDebug_obstacle_blocked(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  ::my_robot_description::msg::SafetyDebug obstacle_blocked(::my_robot_description::msg::SafetyDebug::_obstacle_blocked_type arg)
  {
    msg_.obstacle_blocked = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_front_right_clearance
{
public:
  explicit Init_SafetyDebug_front_right_clearance(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_obstacle_blocked front_right_clearance(::my_robot_description::msg::SafetyDebug::_front_right_clearance_type arg)
  {
    msg_.front_right_clearance = std::move(arg);
    return Init_SafetyDebug_obstacle_blocked(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_front_left_clearance
{
public:
  explicit Init_SafetyDebug_front_left_clearance(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_front_right_clearance front_left_clearance(::my_robot_description::msg::SafetyDebug::_front_left_clearance_type arg)
  {
    msg_.front_left_clearance = std::move(arg);
    return Init_SafetyDebug_front_right_clearance(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_rear_clearance
{
public:
  explicit Init_SafetyDebug_rear_clearance(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_front_left_clearance rear_clearance(::my_robot_description::msg::SafetyDebug::_rear_clearance_type arg)
  {
    msg_.rear_clearance = std::move(arg);
    return Init_SafetyDebug_front_left_clearance(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_front_clearance
{
public:
  explicit Init_SafetyDebug_front_clearance(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_rear_clearance front_clearance(::my_robot_description::msg::SafetyDebug::_front_clearance_type arg)
  {
    msg_.front_clearance = std::move(arg);
    return Init_SafetyDebug_rear_clearance(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_front_right_range
{
public:
  explicit Init_SafetyDebug_front_right_range(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_front_clearance front_right_range(::my_robot_description::msg::SafetyDebug::_front_right_range_type arg)
  {
    msg_.front_right_range = std::move(arg);
    return Init_SafetyDebug_front_clearance(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_front_left_range
{
public:
  explicit Init_SafetyDebug_front_left_range(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_front_right_range front_left_range(::my_robot_description::msg::SafetyDebug::_front_left_range_type arg)
  {
    msg_.front_left_range = std::move(arg);
    return Init_SafetyDebug_front_right_range(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_rear_range
{
public:
  explicit Init_SafetyDebug_rear_range(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_front_left_range rear_range(::my_robot_description::msg::SafetyDebug::_rear_range_type arg)
  {
    msg_.rear_range = std::move(arg);
    return Init_SafetyDebug_front_left_range(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_front_range
{
public:
  explicit Init_SafetyDebug_front_range(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_rear_range front_range(::my_robot_description::msg::SafetyDebug::_front_range_type arg)
  {
    msg_.front_range = std::move(arg);
    return Init_SafetyDebug_rear_range(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_current_angular
{
public:
  explicit Init_SafetyDebug_current_angular(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_front_range current_angular(::my_robot_description::msg::SafetyDebug::_current_angular_type arg)
  {
    msg_.current_angular = std::move(arg);
    return Init_SafetyDebug_front_range(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_current_linear
{
public:
  explicit Init_SafetyDebug_current_linear(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_current_angular current_linear(::my_robot_description::msg::SafetyDebug::_current_linear_type arg)
  {
    msg_.current_linear = std::move(arg);
    return Init_SafetyDebug_current_angular(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_target_angular_after_avoid
{
public:
  explicit Init_SafetyDebug_target_angular_after_avoid(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_current_linear target_angular_after_avoid(::my_robot_description::msg::SafetyDebug::_target_angular_after_avoid_type arg)
  {
    msg_.target_angular_after_avoid = std::move(arg);
    return Init_SafetyDebug_current_linear(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_target_linear_after_safety
{
public:
  explicit Init_SafetyDebug_target_linear_after_safety(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_target_angular_after_avoid target_linear_after_safety(::my_robot_description::msg::SafetyDebug::_target_linear_after_safety_type arg)
  {
    msg_.target_linear_after_safety = std::move(arg);
    return Init_SafetyDebug_target_angular_after_avoid(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_cmd_angular
{
public:
  explicit Init_SafetyDebug_cmd_angular(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_target_linear_after_safety cmd_angular(::my_robot_description::msg::SafetyDebug::_cmd_angular_type arg)
  {
    msg_.cmd_angular = std::move(arg);
    return Init_SafetyDebug_target_linear_after_safety(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_cmd_linear
{
public:
  explicit Init_SafetyDebug_cmd_linear(::my_robot_description::msg::SafetyDebug & msg)
  : msg_(msg)
  {}
  Init_SafetyDebug_cmd_angular cmd_linear(::my_robot_description::msg::SafetyDebug::_cmd_linear_type arg)
  {
    msg_.cmd_linear = std::move(arg);
    return Init_SafetyDebug_cmd_angular(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

class Init_SafetyDebug_stamp
{
public:
  Init_SafetyDebug_stamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SafetyDebug_cmd_linear stamp(::my_robot_description::msg::SafetyDebug::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return Init_SafetyDebug_cmd_linear(msg_);
  }

private:
  ::my_robot_description::msg::SafetyDebug msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_description::msg::SafetyDebug>()
{
  return my_robot_description::msg::builder::Init_SafetyDebug_stamp();
}

}  // namespace my_robot_description

#endif  // MY_ROBOT_DESCRIPTION__MSG__DETAIL__SAFETY_DEBUG__BUILDER_HPP_
