// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_robot_description:msg/WallFollowDebug.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "my_robot_description/msg/wall_follow_debug.hpp"


#ifndef MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__TRAITS_HPP_
#define MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_robot_description/msg/detail/wall_follow_debug__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace my_robot_description
{

namespace msg
{

inline void to_flow_style_yaml(
  const WallFollowDebug & msg,
  std::ostream & out)
{
  out << "{";
  // member: stamp
  {
    out << "stamp: ";
    to_flow_style_yaml(msg.stamp, out);
    out << ", ";
  }

  // member: state
  {
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << ", ";
  }

  // member: front_range
  {
    out << "front_range: ";
    rosidl_generator_traits::value_to_yaml(msg.front_range, out);
    out << ", ";
  }

  // member: side_range
  {
    out << "side_range: ";
    rosidl_generator_traits::value_to_yaml(msg.side_range, out);
    out << ", ";
  }

  // member: diagonal_range
  {
    out << "diagonal_range: ";
    rosidl_generator_traits::value_to_yaml(msg.diagonal_range, out);
    out << ", ";
  }

  // member: distance_error
  {
    out << "distance_error: ";
    rosidl_generator_traits::value_to_yaml(msg.distance_error, out);
    out << ", ";
  }

  // member: wall_angle_error
  {
    out << "wall_angle_error: ";
    rosidl_generator_traits::value_to_yaml(msg.wall_angle_error, out);
    out << ", ";
  }

  // member: front_speed_scale
  {
    out << "front_speed_scale: ";
    rosidl_generator_traits::value_to_yaml(msg.front_speed_scale, out);
    out << ", ";
  }

  // member: linear_command
  {
    out << "linear_command: ";
    rosidl_generator_traits::value_to_yaml(msg.linear_command, out);
    out << ", ";
  }

  // member: angular_command
  {
    out << "angular_command: ";
    rosidl_generator_traits::value_to_yaml(msg.angular_command, out);
    out << ", ";
  }

  // member: front_blocked
  {
    out << "front_blocked: ";
    rosidl_generator_traits::value_to_yaml(msg.front_blocked, out);
    out << ", ";
  }

  // member: wall_lost
  {
    out << "wall_lost: ";
    rosidl_generator_traits::value_to_yaml(msg.wall_lost, out);
    out << ", ";
  }

  // member: in_acquire_mode
  {
    out << "in_acquire_mode: ";
    rosidl_generator_traits::value_to_yaml(msg.in_acquire_mode, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const WallFollowDebug & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_block_style_yaml(msg.stamp, out, indentation + 2);
  }

  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << "\n";
  }

  // member: front_range
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "front_range: ";
    rosidl_generator_traits::value_to_yaml(msg.front_range, out);
    out << "\n";
  }

  // member: side_range
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "side_range: ";
    rosidl_generator_traits::value_to_yaml(msg.side_range, out);
    out << "\n";
  }

  // member: diagonal_range
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "diagonal_range: ";
    rosidl_generator_traits::value_to_yaml(msg.diagonal_range, out);
    out << "\n";
  }

  // member: distance_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance_error: ";
    rosidl_generator_traits::value_to_yaml(msg.distance_error, out);
    out << "\n";
  }

  // member: wall_angle_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "wall_angle_error: ";
    rosidl_generator_traits::value_to_yaml(msg.wall_angle_error, out);
    out << "\n";
  }

  // member: front_speed_scale
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "front_speed_scale: ";
    rosidl_generator_traits::value_to_yaml(msg.front_speed_scale, out);
    out << "\n";
  }

  // member: linear_command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "linear_command: ";
    rosidl_generator_traits::value_to_yaml(msg.linear_command, out);
    out << "\n";
  }

  // member: angular_command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angular_command: ";
    rosidl_generator_traits::value_to_yaml(msg.angular_command, out);
    out << "\n";
  }

  // member: front_blocked
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "front_blocked: ";
    rosidl_generator_traits::value_to_yaml(msg.front_blocked, out);
    out << "\n";
  }

  // member: wall_lost
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "wall_lost: ";
    rosidl_generator_traits::value_to_yaml(msg.wall_lost, out);
    out << "\n";
  }

  // member: in_acquire_mode
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "in_acquire_mode: ";
    rosidl_generator_traits::value_to_yaml(msg.in_acquire_mode, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const WallFollowDebug & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace my_robot_description

namespace rosidl_generator_traits
{

[[deprecated("use my_robot_description::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_robot_description::msg::WallFollowDebug & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_robot_description::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_robot_description::msg::to_yaml() instead")]]
inline std::string to_yaml(const my_robot_description::msg::WallFollowDebug & msg)
{
  return my_robot_description::msg::to_yaml(msg);
}

template<>
inline const char * data_type<my_robot_description::msg::WallFollowDebug>()
{
  return "my_robot_description::msg::WallFollowDebug";
}

template<>
inline const char * name<my_robot_description::msg::WallFollowDebug>()
{
  return "my_robot_description/msg/WallFollowDebug";
}

template<>
struct has_fixed_size<my_robot_description::msg::WallFollowDebug>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<my_robot_description::msg::WallFollowDebug>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<my_robot_description::msg::WallFollowDebug>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__TRAITS_HPP_
