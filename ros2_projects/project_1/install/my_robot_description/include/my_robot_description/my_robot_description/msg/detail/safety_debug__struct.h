// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_robot_description:msg/SafetyDebug.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "my_robot_description/msg/safety_debug.h"


#ifndef MY_ROBOT_DESCRIPTION__MSG__DETAIL__SAFETY_DEBUG__STRUCT_H_
#define MY_ROBOT_DESCRIPTION__MSG__DETAIL__SAFETY_DEBUG__STRUCT_H_

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

/// Struct defined in msg/SafetyDebug in the package my_robot_description.
typedef struct my_robot_description__msg__SafetyDebug
{
  builtin_interfaces__msg__Time stamp;
  float cmd_linear;
  float cmd_angular;
  float target_linear_after_safety;
  float target_angular_after_avoid;
  float current_linear;
  float current_angular;
  float front_range;
  float rear_range;
  float front_left_range;
  float front_right_range;
  float front_clearance;
  float rear_clearance;
  float front_left_clearance;
  float front_right_clearance;
  bool obstacle_blocked;
} my_robot_description__msg__SafetyDebug;

// Struct for a sequence of my_robot_description__msg__SafetyDebug.
typedef struct my_robot_description__msg__SafetyDebug__Sequence
{
  my_robot_description__msg__SafetyDebug * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_description__msg__SafetyDebug__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_ROBOT_DESCRIPTION__MSG__DETAIL__SAFETY_DEBUG__STRUCT_H_
