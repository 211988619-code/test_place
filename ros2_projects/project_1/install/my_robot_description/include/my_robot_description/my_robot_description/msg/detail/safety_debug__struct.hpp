// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_robot_description:msg/SafetyDebug.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "my_robot_description/msg/safety_debug.hpp"


#ifndef MY_ROBOT_DESCRIPTION__MSG__DETAIL__SAFETY_DEBUG__STRUCT_HPP_
#define MY_ROBOT_DESCRIPTION__MSG__DETAIL__SAFETY_DEBUG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__my_robot_description__msg__SafetyDebug __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_description__msg__SafetyDebug __declspec(deprecated)
#endif

namespace my_robot_description
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct SafetyDebug_
{
  using Type = SafetyDebug_<ContainerAllocator>;

  explicit SafetyDebug_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cmd_linear = 0.0f;
      this->cmd_angular = 0.0f;
      this->target_linear_after_safety = 0.0f;
      this->target_angular_after_avoid = 0.0f;
      this->current_linear = 0.0f;
      this->current_angular = 0.0f;
      this->front_range = 0.0f;
      this->rear_range = 0.0f;
      this->front_left_range = 0.0f;
      this->front_right_range = 0.0f;
      this->front_clearance = 0.0f;
      this->rear_clearance = 0.0f;
      this->front_left_clearance = 0.0f;
      this->front_right_clearance = 0.0f;
      this->obstacle_blocked = false;
    }
  }

  explicit SafetyDebug_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cmd_linear = 0.0f;
      this->cmd_angular = 0.0f;
      this->target_linear_after_safety = 0.0f;
      this->target_angular_after_avoid = 0.0f;
      this->current_linear = 0.0f;
      this->current_angular = 0.0f;
      this->front_range = 0.0f;
      this->rear_range = 0.0f;
      this->front_left_range = 0.0f;
      this->front_right_range = 0.0f;
      this->front_clearance = 0.0f;
      this->rear_clearance = 0.0f;
      this->front_left_clearance = 0.0f;
      this->front_right_clearance = 0.0f;
      this->obstacle_blocked = false;
    }
  }

  // field types and members
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;
  using _cmd_linear_type =
    float;
  _cmd_linear_type cmd_linear;
  using _cmd_angular_type =
    float;
  _cmd_angular_type cmd_angular;
  using _target_linear_after_safety_type =
    float;
  _target_linear_after_safety_type target_linear_after_safety;
  using _target_angular_after_avoid_type =
    float;
  _target_angular_after_avoid_type target_angular_after_avoid;
  using _current_linear_type =
    float;
  _current_linear_type current_linear;
  using _current_angular_type =
    float;
  _current_angular_type current_angular;
  using _front_range_type =
    float;
  _front_range_type front_range;
  using _rear_range_type =
    float;
  _rear_range_type rear_range;
  using _front_left_range_type =
    float;
  _front_left_range_type front_left_range;
  using _front_right_range_type =
    float;
  _front_right_range_type front_right_range;
  using _front_clearance_type =
    float;
  _front_clearance_type front_clearance;
  using _rear_clearance_type =
    float;
  _rear_clearance_type rear_clearance;
  using _front_left_clearance_type =
    float;
  _front_left_clearance_type front_left_clearance;
  using _front_right_clearance_type =
    float;
  _front_right_clearance_type front_right_clearance;
  using _obstacle_blocked_type =
    bool;
  _obstacle_blocked_type obstacle_blocked;

  // setters for named parameter idiom
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }
  Type & set__cmd_linear(
    const float & _arg)
  {
    this->cmd_linear = _arg;
    return *this;
  }
  Type & set__cmd_angular(
    const float & _arg)
  {
    this->cmd_angular = _arg;
    return *this;
  }
  Type & set__target_linear_after_safety(
    const float & _arg)
  {
    this->target_linear_after_safety = _arg;
    return *this;
  }
  Type & set__target_angular_after_avoid(
    const float & _arg)
  {
    this->target_angular_after_avoid = _arg;
    return *this;
  }
  Type & set__current_linear(
    const float & _arg)
  {
    this->current_linear = _arg;
    return *this;
  }
  Type & set__current_angular(
    const float & _arg)
  {
    this->current_angular = _arg;
    return *this;
  }
  Type & set__front_range(
    const float & _arg)
  {
    this->front_range = _arg;
    return *this;
  }
  Type & set__rear_range(
    const float & _arg)
  {
    this->rear_range = _arg;
    return *this;
  }
  Type & set__front_left_range(
    const float & _arg)
  {
    this->front_left_range = _arg;
    return *this;
  }
  Type & set__front_right_range(
    const float & _arg)
  {
    this->front_right_range = _arg;
    return *this;
  }
  Type & set__front_clearance(
    const float & _arg)
  {
    this->front_clearance = _arg;
    return *this;
  }
  Type & set__rear_clearance(
    const float & _arg)
  {
    this->rear_clearance = _arg;
    return *this;
  }
  Type & set__front_left_clearance(
    const float & _arg)
  {
    this->front_left_clearance = _arg;
    return *this;
  }
  Type & set__front_right_clearance(
    const float & _arg)
  {
    this->front_right_clearance = _arg;
    return *this;
  }
  Type & set__obstacle_blocked(
    const bool & _arg)
  {
    this->obstacle_blocked = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_description::msg::SafetyDebug_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_description::msg::SafetyDebug_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_description::msg::SafetyDebug_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_description::msg::SafetyDebug_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_description::msg::SafetyDebug_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_description::msg::SafetyDebug_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_description::msg::SafetyDebug_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_description::msg::SafetyDebug_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_description::msg::SafetyDebug_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_description::msg::SafetyDebug_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_description__msg__SafetyDebug
    std::shared_ptr<my_robot_description::msg::SafetyDebug_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_description__msg__SafetyDebug
    std::shared_ptr<my_robot_description::msg::SafetyDebug_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SafetyDebug_ & other) const
  {
    if (this->stamp != other.stamp) {
      return false;
    }
    if (this->cmd_linear != other.cmd_linear) {
      return false;
    }
    if (this->cmd_angular != other.cmd_angular) {
      return false;
    }
    if (this->target_linear_after_safety != other.target_linear_after_safety) {
      return false;
    }
    if (this->target_angular_after_avoid != other.target_angular_after_avoid) {
      return false;
    }
    if (this->current_linear != other.current_linear) {
      return false;
    }
    if (this->current_angular != other.current_angular) {
      return false;
    }
    if (this->front_range != other.front_range) {
      return false;
    }
    if (this->rear_range != other.rear_range) {
      return false;
    }
    if (this->front_left_range != other.front_left_range) {
      return false;
    }
    if (this->front_right_range != other.front_right_range) {
      return false;
    }
    if (this->front_clearance != other.front_clearance) {
      return false;
    }
    if (this->rear_clearance != other.rear_clearance) {
      return false;
    }
    if (this->front_left_clearance != other.front_left_clearance) {
      return false;
    }
    if (this->front_right_clearance != other.front_right_clearance) {
      return false;
    }
    if (this->obstacle_blocked != other.obstacle_blocked) {
      return false;
    }
    return true;
  }
  bool operator!=(const SafetyDebug_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SafetyDebug_

// alias to use template instance with default allocator
using SafetyDebug =
  my_robot_description::msg::SafetyDebug_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace my_robot_description

#endif  // MY_ROBOT_DESCRIPTION__MSG__DETAIL__SAFETY_DEBUG__STRUCT_HPP_
