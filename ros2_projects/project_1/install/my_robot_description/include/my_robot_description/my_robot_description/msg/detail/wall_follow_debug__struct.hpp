// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_robot_description:msg/WallFollowDebug.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "my_robot_description/msg/wall_follow_debug.hpp"


#ifndef MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__STRUCT_HPP_
#define MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__STRUCT_HPP_

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
# define DEPRECATED__my_robot_description__msg__WallFollowDebug __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_description__msg__WallFollowDebug __declspec(deprecated)
#endif

namespace my_robot_description
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct WallFollowDebug_
{
  using Type = WallFollowDebug_<ContainerAllocator>;

  explicit WallFollowDebug_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->state = "";
      this->front_range = 0.0f;
      this->side_range = 0.0f;
      this->diagonal_range = 0.0f;
      this->distance_error = 0.0f;
      this->wall_angle_error = 0.0f;
      this->front_speed_scale = 0.0f;
      this->linear_command = 0.0f;
      this->angular_command = 0.0f;
      this->front_blocked = false;
      this->wall_lost = false;
      this->in_acquire_mode = false;
    }
  }

  explicit WallFollowDebug_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init),
    state(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->state = "";
      this->front_range = 0.0f;
      this->side_range = 0.0f;
      this->diagonal_range = 0.0f;
      this->distance_error = 0.0f;
      this->wall_angle_error = 0.0f;
      this->front_speed_scale = 0.0f;
      this->linear_command = 0.0f;
      this->angular_command = 0.0f;
      this->front_blocked = false;
      this->wall_lost = false;
      this->in_acquire_mode = false;
    }
  }

  // field types and members
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;
  using _state_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _state_type state;
  using _front_range_type =
    float;
  _front_range_type front_range;
  using _side_range_type =
    float;
  _side_range_type side_range;
  using _diagonal_range_type =
    float;
  _diagonal_range_type diagonal_range;
  using _distance_error_type =
    float;
  _distance_error_type distance_error;
  using _wall_angle_error_type =
    float;
  _wall_angle_error_type wall_angle_error;
  using _front_speed_scale_type =
    float;
  _front_speed_scale_type front_speed_scale;
  using _linear_command_type =
    float;
  _linear_command_type linear_command;
  using _angular_command_type =
    float;
  _angular_command_type angular_command;
  using _front_blocked_type =
    bool;
  _front_blocked_type front_blocked;
  using _wall_lost_type =
    bool;
  _wall_lost_type wall_lost;
  using _in_acquire_mode_type =
    bool;
  _in_acquire_mode_type in_acquire_mode;

  // setters for named parameter idiom
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }
  Type & set__state(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->state = _arg;
    return *this;
  }
  Type & set__front_range(
    const float & _arg)
  {
    this->front_range = _arg;
    return *this;
  }
  Type & set__side_range(
    const float & _arg)
  {
    this->side_range = _arg;
    return *this;
  }
  Type & set__diagonal_range(
    const float & _arg)
  {
    this->diagonal_range = _arg;
    return *this;
  }
  Type & set__distance_error(
    const float & _arg)
  {
    this->distance_error = _arg;
    return *this;
  }
  Type & set__wall_angle_error(
    const float & _arg)
  {
    this->wall_angle_error = _arg;
    return *this;
  }
  Type & set__front_speed_scale(
    const float & _arg)
  {
    this->front_speed_scale = _arg;
    return *this;
  }
  Type & set__linear_command(
    const float & _arg)
  {
    this->linear_command = _arg;
    return *this;
  }
  Type & set__angular_command(
    const float & _arg)
  {
    this->angular_command = _arg;
    return *this;
  }
  Type & set__front_blocked(
    const bool & _arg)
  {
    this->front_blocked = _arg;
    return *this;
  }
  Type & set__wall_lost(
    const bool & _arg)
  {
    this->wall_lost = _arg;
    return *this;
  }
  Type & set__in_acquire_mode(
    const bool & _arg)
  {
    this->in_acquire_mode = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_description::msg::WallFollowDebug_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_description::msg::WallFollowDebug_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_description::msg::WallFollowDebug_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_description::msg::WallFollowDebug_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_description::msg::WallFollowDebug_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_description::msg::WallFollowDebug_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_description::msg::WallFollowDebug_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_description::msg::WallFollowDebug_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_description::msg::WallFollowDebug_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_description::msg::WallFollowDebug_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_description__msg__WallFollowDebug
    std::shared_ptr<my_robot_description::msg::WallFollowDebug_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_description__msg__WallFollowDebug
    std::shared_ptr<my_robot_description::msg::WallFollowDebug_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WallFollowDebug_ & other) const
  {
    if (this->stamp != other.stamp) {
      return false;
    }
    if (this->state != other.state) {
      return false;
    }
    if (this->front_range != other.front_range) {
      return false;
    }
    if (this->side_range != other.side_range) {
      return false;
    }
    if (this->diagonal_range != other.diagonal_range) {
      return false;
    }
    if (this->distance_error != other.distance_error) {
      return false;
    }
    if (this->wall_angle_error != other.wall_angle_error) {
      return false;
    }
    if (this->front_speed_scale != other.front_speed_scale) {
      return false;
    }
    if (this->linear_command != other.linear_command) {
      return false;
    }
    if (this->angular_command != other.angular_command) {
      return false;
    }
    if (this->front_blocked != other.front_blocked) {
      return false;
    }
    if (this->wall_lost != other.wall_lost) {
      return false;
    }
    if (this->in_acquire_mode != other.in_acquire_mode) {
      return false;
    }
    return true;
  }
  bool operator!=(const WallFollowDebug_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WallFollowDebug_

// alias to use template instance with default allocator
using WallFollowDebug =
  my_robot_description::msg::WallFollowDebug_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace my_robot_description

#endif  // MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__STRUCT_HPP_
