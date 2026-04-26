// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from my_robot_description:msg/WallFollowDebug.idl
// generated code does not contain a copyright notice
#ifndef MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "my_robot_description/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "my_robot_description/msg/detail/wall_follow_debug__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_my_robot_description
bool cdr_serialize_my_robot_description__msg__WallFollowDebug(
  const my_robot_description__msg__WallFollowDebug * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_my_robot_description
bool cdr_deserialize_my_robot_description__msg__WallFollowDebug(
  eprosima::fastcdr::Cdr &,
  my_robot_description__msg__WallFollowDebug * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_my_robot_description
size_t get_serialized_size_my_robot_description__msg__WallFollowDebug(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_my_robot_description
size_t max_serialized_size_my_robot_description__msg__WallFollowDebug(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_my_robot_description
bool cdr_serialize_key_my_robot_description__msg__WallFollowDebug(
  const my_robot_description__msg__WallFollowDebug * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_my_robot_description
size_t get_serialized_size_key_my_robot_description__msg__WallFollowDebug(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_my_robot_description
size_t max_serialized_size_key_my_robot_description__msg__WallFollowDebug(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_my_robot_description
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, my_robot_description, msg, WallFollowDebug)();

#ifdef __cplusplus
}
#endif

#endif  // MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
