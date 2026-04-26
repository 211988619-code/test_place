// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from my_robot_description:msg/WallFollowDebug.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include <cstddef>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "my_robot_description/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "my_robot_description/msg/detail/wall_follow_debug__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace my_robot_description
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_my_robot_description
cdr_serialize(
  const my_robot_description::msg::WallFollowDebug & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_my_robot_description
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  my_robot_description::msg::WallFollowDebug & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_my_robot_description
get_serialized_size(
  const my_robot_description::msg::WallFollowDebug & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_my_robot_description
max_serialized_size_WallFollowDebug(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_my_robot_description
cdr_serialize_key(
  const my_robot_description::msg::WallFollowDebug & ros_message,
  eprosima::fastcdr::Cdr &);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_my_robot_description
get_serialized_size_key(
  const my_robot_description::msg::WallFollowDebug & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_my_robot_description
max_serialized_size_key_WallFollowDebug(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace my_robot_description

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_my_robot_description
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, my_robot_description, msg, WallFollowDebug)();

#ifdef __cplusplus
}
#endif

#endif  // MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
