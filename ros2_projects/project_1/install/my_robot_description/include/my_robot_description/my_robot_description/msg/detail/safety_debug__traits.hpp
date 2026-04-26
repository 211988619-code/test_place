// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_robot_description:msg/SafetyDebug.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "my_robot_description/msg/safety_debug.hpp"


#ifndef MY_ROBOT_DESCRIPTION__MSG__DETAIL__SAFETY_DEBUG__TRAITS_HPP_
#define MY_ROBOT_DESCRIPTION__MSG__DETAIL__SAFETY_DEBUG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_robot_description/msg/detail/safety_debug__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace my_robot_description
{

namespace msg
{

inline void to_flow_style_yaml(
  const SafetyDebug & msg,
  std::ostream & out)
{
  out << "{";
  // member: stamp
  {
    out << "stamp: ";
    to_flow_style_yaml(msg.stamp, out);
    out << ", ";
  }

  // member: cmd_linear
  {
    out << "cmd_linear: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd_linear, out);
    out << ", ";
  }

  // member: cmd_angular
  {
    out << "cmd_angular: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd_angular, out);
    out << ", ";
  }

  // member: target_linear_after_safety
  {
    out << "target_linear_after_safety: ";
    rosidl_generator_traits::value_to_yaml(msg.target_linear_after_safety, out);
    out << ", ";
  }

  // member: target_angular_after_avoid
  {
    out << "target_angular_after_avoid: ";
    rosidl_generator_traits::value_to_yaml(msg.target_angular_after_avoid, out);
    out << ", ";
  }

  // member: current_linear
  {
    out << "current_linear: ";
    rosidl_generator_traits::value_to_yaml(msg.current_linear, out);
    out << ", ";
  }

  // member: current_angular
  {
    out << "current_angular: ";
    rosidl_generator_traits::value_to_yaml(msg.current_angular, out);
    out << ", ";
  }

  // member: front_range
  {
    out << "front_range: ";
    rosidl_generator_traits::value_to_yaml(msg.front_range, out);
    out << ", ";
  }

  // member: rear_range
  {
    out << "rear_range: ";
    rosidl_generator_traits::value_to_yaml(msg.rear_range, out);
    out << ", ";
  }

  // member: front_left_range
  {
    out << "front_left_range: ";
    rosidl_generator_traits::value_to_yaml(msg.front_left_range, out);
    out << ", ";
  }

  // member: front_right_range
  {
    out << "front_right_range: ";
    rosidl_generator_traits::value_to_yaml(msg.front_right_range, out);
    out << ", ";
  }

  // member: front_clearance
  {
    out << "front_clearance: ";
    rosidl_generator_traits::value_to_yaml(msg.front_clearance, out);
    out << ", ";
  }

  // member: rear_clearance
  {
    out << "rear_clearance: ";
    rosidl_generator_traits::value_to_yaml(msg.rear_clearance, out);
    out << ", ";
  }

  // member: front_left_clearance
  {
    out << "front_left_clearance: ";
    rosidl_generator_traits::value_to_yaml(msg.front_left_clearance, out);
    out << ", ";
  }

  // member: front_right_clearance
  {
    out << "front_right_clearance: ";
    rosidl_generator_traits::value_to_yaml(msg.front_right_clearance, out);
    out << ", ";
  }

  // member: obstacle_blocked
  {
    out << "obstacle_blocked: ";
    rosidl_generator_traits::value_to_yaml(msg.obstacle_blocked, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SafetyDebug & msg,
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

  // member: cmd_linear
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cmd_linear: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd_linear, out);
    out << "\n";
  }

  // member: cmd_angular
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cmd_angular: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd_angular, out);
    out << "\n";
  }

  // member: target_linear_after_safety
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_linear_after_safety: ";
    rosidl_generator_traits::value_to_yaml(msg.target_linear_after_safety, out);
    out << "\n";
  }

  // member: target_angular_after_avoid
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_angular_after_avoid: ";
    rosidl_generator_traits::value_to_yaml(msg.target_angular_after_avoid, out);
    out << "\n";
  }

  // member: current_linear
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_linear: ";
    rosidl_generator_traits::value_to_yaml(msg.current_linear, out);
    out << "\n";
  }

  // member: current_angular
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_angular: ";
    rosidl_generator_traits::value_to_yaml(msg.current_angular, out);
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

  // member: rear_range
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rear_range: ";
    rosidl_generator_traits::value_to_yaml(msg.rear_range, out);
    out << "\n";
  }

  // member: front_left_range
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "front_left_range: ";
    rosidl_generator_traits::value_to_yaml(msg.front_left_range, out);
    out << "\n";
  }

  // member: front_right_range
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "front_right_range: ";
    rosidl_generator_traits::value_to_yaml(msg.front_right_range, out);
    out << "\n";
  }

  // member: front_clearance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "front_clearance: ";
    rosidl_generator_traits::value_to_yaml(msg.front_clearance, out);
    out << "\n";
  }

  // member: rear_clearance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rear_clearance: ";
    rosidl_generator_traits::value_to_yaml(msg.rear_clearance, out);
    out << "\n";
  }

  // member: front_left_clearance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "front_left_clearance: ";
    rosidl_generator_traits::value_to_yaml(msg.front_left_clearance, out);
    out << "\n";
  }

  // member: front_right_clearance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "front_right_clearance: ";
    rosidl_generator_traits::value_to_yaml(msg.front_right_clearance, out);
    out << "\n";
  }

  // member: obstacle_blocked
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "obstacle_blocked: ";
    rosidl_generator_traits::value_to_yaml(msg.obstacle_blocked, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SafetyDebug & msg, bool use_flow_style = false)
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
  const my_robot_description::msg::SafetyDebug & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_robot_description::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_robot_description::msg::to_yaml() instead")]]
inline std::string to_yaml(const my_robot_description::msg::SafetyDebug & msg)
{
  return my_robot_description::msg::to_yaml(msg);
}

template<>
inline const char * data_type<my_robot_description::msg::SafetyDebug>()
{
  return "my_robot_description::msg::SafetyDebug";
}

template<>
inline const char * name<my_robot_description::msg::SafetyDebug>()
{
  return "my_robot_description/msg/SafetyDebug";
}

template<>
struct has_fixed_size<my_robot_description::msg::SafetyDebug>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<my_robot_description::msg::SafetyDebug>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<my_robot_description::msg::SafetyDebug>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MY_ROBOT_DESCRIPTION__MSG__DETAIL__SAFETY_DEBUG__TRAITS_HPP_
