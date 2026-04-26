// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from my_robot_description:msg/WallFollowDebug.idl
// generated code does not contain a copyright notice
#include "my_robot_description/msg/detail/wall_follow_debug__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"
// Member `state`
#include "rosidl_runtime_c/string_functions.h"

bool
my_robot_description__msg__WallFollowDebug__init(my_robot_description__msg__WallFollowDebug * msg)
{
  if (!msg) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    my_robot_description__msg__WallFollowDebug__fini(msg);
    return false;
  }
  // state
  if (!rosidl_runtime_c__String__init(&msg->state)) {
    my_robot_description__msg__WallFollowDebug__fini(msg);
    return false;
  }
  // front_range
  // side_range
  // diagonal_range
  // distance_error
  // wall_angle_error
  // front_speed_scale
  // linear_command
  // angular_command
  // front_blocked
  // wall_lost
  // in_acquire_mode
  return true;
}

void
my_robot_description__msg__WallFollowDebug__fini(my_robot_description__msg__WallFollowDebug * msg)
{
  if (!msg) {
    return;
  }
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
  // state
  rosidl_runtime_c__String__fini(&msg->state);
  // front_range
  // side_range
  // diagonal_range
  // distance_error
  // wall_angle_error
  // front_speed_scale
  // linear_command
  // angular_command
  // front_blocked
  // wall_lost
  // in_acquire_mode
}

bool
my_robot_description__msg__WallFollowDebug__are_equal(const my_robot_description__msg__WallFollowDebug * lhs, const my_robot_description__msg__WallFollowDebug * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->stamp), &(rhs->stamp)))
  {
    return false;
  }
  // state
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->state), &(rhs->state)))
  {
    return false;
  }
  // front_range
  if (lhs->front_range != rhs->front_range) {
    return false;
  }
  // side_range
  if (lhs->side_range != rhs->side_range) {
    return false;
  }
  // diagonal_range
  if (lhs->diagonal_range != rhs->diagonal_range) {
    return false;
  }
  // distance_error
  if (lhs->distance_error != rhs->distance_error) {
    return false;
  }
  // wall_angle_error
  if (lhs->wall_angle_error != rhs->wall_angle_error) {
    return false;
  }
  // front_speed_scale
  if (lhs->front_speed_scale != rhs->front_speed_scale) {
    return false;
  }
  // linear_command
  if (lhs->linear_command != rhs->linear_command) {
    return false;
  }
  // angular_command
  if (lhs->angular_command != rhs->angular_command) {
    return false;
  }
  // front_blocked
  if (lhs->front_blocked != rhs->front_blocked) {
    return false;
  }
  // wall_lost
  if (lhs->wall_lost != rhs->wall_lost) {
    return false;
  }
  // in_acquire_mode
  if (lhs->in_acquire_mode != rhs->in_acquire_mode) {
    return false;
  }
  return true;
}

bool
my_robot_description__msg__WallFollowDebug__copy(
  const my_robot_description__msg__WallFollowDebug * input,
  my_robot_description__msg__WallFollowDebug * output)
{
  if (!input || !output) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->stamp), &(output->stamp)))
  {
    return false;
  }
  // state
  if (!rosidl_runtime_c__String__copy(
      &(input->state), &(output->state)))
  {
    return false;
  }
  // front_range
  output->front_range = input->front_range;
  // side_range
  output->side_range = input->side_range;
  // diagonal_range
  output->diagonal_range = input->diagonal_range;
  // distance_error
  output->distance_error = input->distance_error;
  // wall_angle_error
  output->wall_angle_error = input->wall_angle_error;
  // front_speed_scale
  output->front_speed_scale = input->front_speed_scale;
  // linear_command
  output->linear_command = input->linear_command;
  // angular_command
  output->angular_command = input->angular_command;
  // front_blocked
  output->front_blocked = input->front_blocked;
  // wall_lost
  output->wall_lost = input->wall_lost;
  // in_acquire_mode
  output->in_acquire_mode = input->in_acquire_mode;
  return true;
}

my_robot_description__msg__WallFollowDebug *
my_robot_description__msg__WallFollowDebug__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_robot_description__msg__WallFollowDebug * msg = (my_robot_description__msg__WallFollowDebug *)allocator.allocate(sizeof(my_robot_description__msg__WallFollowDebug), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(my_robot_description__msg__WallFollowDebug));
  bool success = my_robot_description__msg__WallFollowDebug__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
my_robot_description__msg__WallFollowDebug__destroy(my_robot_description__msg__WallFollowDebug * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    my_robot_description__msg__WallFollowDebug__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
my_robot_description__msg__WallFollowDebug__Sequence__init(my_robot_description__msg__WallFollowDebug__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_robot_description__msg__WallFollowDebug * data = NULL;

  if (size) {
    data = (my_robot_description__msg__WallFollowDebug *)allocator.zero_allocate(size, sizeof(my_robot_description__msg__WallFollowDebug), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = my_robot_description__msg__WallFollowDebug__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        my_robot_description__msg__WallFollowDebug__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
my_robot_description__msg__WallFollowDebug__Sequence__fini(my_robot_description__msg__WallFollowDebug__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      my_robot_description__msg__WallFollowDebug__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

my_robot_description__msg__WallFollowDebug__Sequence *
my_robot_description__msg__WallFollowDebug__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_robot_description__msg__WallFollowDebug__Sequence * array = (my_robot_description__msg__WallFollowDebug__Sequence *)allocator.allocate(sizeof(my_robot_description__msg__WallFollowDebug__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = my_robot_description__msg__WallFollowDebug__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
my_robot_description__msg__WallFollowDebug__Sequence__destroy(my_robot_description__msg__WallFollowDebug__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    my_robot_description__msg__WallFollowDebug__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
my_robot_description__msg__WallFollowDebug__Sequence__are_equal(const my_robot_description__msg__WallFollowDebug__Sequence * lhs, const my_robot_description__msg__WallFollowDebug__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!my_robot_description__msg__WallFollowDebug__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
my_robot_description__msg__WallFollowDebug__Sequence__copy(
  const my_robot_description__msg__WallFollowDebug__Sequence * input,
  my_robot_description__msg__WallFollowDebug__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(my_robot_description__msg__WallFollowDebug);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    my_robot_description__msg__WallFollowDebug * data =
      (my_robot_description__msg__WallFollowDebug *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!my_robot_description__msg__WallFollowDebug__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          my_robot_description__msg__WallFollowDebug__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!my_robot_description__msg__WallFollowDebug__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
