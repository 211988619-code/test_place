// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_robot_description:msg/WallFollowDebug.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "my_robot_description/msg/wall_follow_debug.h"


#ifndef MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__STRUCT_H_
#define MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"
// Member 'state'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/WallFollowDebug in the package my_robot_description.
typedef struct my_robot_description__msg__WallFollowDebug
{
  builtin_interfaces__msg__Time stamp;
  rosidl_runtime_c__String state;
  float front_range;
  float side_range;
  float diagonal_range;
  float distance_error;
  float wall_angle_error;
  float front_speed_scale;
  float linear_command;
  float angular_command;
  bool front_blocked;
  bool wall_lost;
  bool in_acquire_mode;
} my_robot_description__msg__WallFollowDebug;

// Struct for a sequence of my_robot_description__msg__WallFollowDebug.
typedef struct my_robot_description__msg__WallFollowDebug__Sequence
{
  my_robot_description__msg__WallFollowDebug * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_description__msg__WallFollowDebug__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_ROBOT_DESCRIPTION__MSG__DETAIL__WALL_FOLLOW_DEBUG__STRUCT_H_
