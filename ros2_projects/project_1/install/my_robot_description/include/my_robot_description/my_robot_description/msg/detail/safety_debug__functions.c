// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from my_robot_description:msg/SafetyDebug.idl
// generated code does not contain a copyright notice
#include "my_robot_description/msg/detail/safety_debug__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
my_robot_description__msg__SafetyDebug__init(my_robot_description__msg__SafetyDebug * msg)
{
  if (!msg) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    my_robot_description__msg__SafetyDebug__fini(msg);
    return false;
  }
  // cmd_linear
  // cmd_angular
  // target_linear_after_safety
  // target_angular_after_avoid
  // current_linear
  // current_angular
  // front_range
  // rear_range
  // front_left_range
  // front_right_range
  // front_clearance
  // rear_clearance
  // front_left_clearance
  // front_right_clearance
  // obstacle_blocked
  return true;
}

void
my_robot_description__msg__SafetyDebug__fini(my_robot_description__msg__SafetyDebug * msg)
{
  if (!msg) {
    return;
  }
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
  // cmd_linear
  // cmd_angular
  // target_linear_after_safety
  // target_angular_after_avoid
  // current_linear
  // current_angular
  // front_range
  // rear_range
  // front_left_range
  // front_right_range
  // front_clearance
  // rear_clearance
  // front_left_clearance
  // front_right_clearance
  // obstacle_blocked
}

bool
my_robot_description__msg__SafetyDebug__are_equal(const my_robot_description__msg__SafetyDebug * lhs, const my_robot_description__msg__SafetyDebug * rhs)
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
  // cmd_linear
  if (lhs->cmd_linear != rhs->cmd_linear) {
    return false;
  }
  // cmd_angular
  if (lhs->cmd_angular != rhs->cmd_angular) {
    return false;
  }
  // target_linear_after_safety
  if (lhs->target_linear_after_safety != rhs->target_linear_after_safety) {
    return false;
  }
  // target_angular_after_avoid
  if (lhs->target_angular_after_avoid != rhs->target_angular_after_avoid) {
    return false;
  }
  // current_linear
  if (lhs->current_linear != rhs->current_linear) {
    return false;
  }
  // current_angular
  if (lhs->current_angular != rhs->current_angular) {
    return false;
  }
  // front_range
  if (lhs->front_range != rhs->front_range) {
    return false;
  }
  // rear_range
  if (lhs->rear_range != rhs->rear_range) {
    return false;
  }
  // front_left_range
  if (lhs->front_left_range != rhs->front_left_range) {
    return false;
  }
  // front_right_range
  if (lhs->front_right_range != rhs->front_right_range) {
    return false;
  }
  // front_clearance
  if (lhs->front_clearance != rhs->front_clearance) {
    return false;
  }
  // rear_clearance
  if (lhs->rear_clearance != rhs->rear_clearance) {
    return false;
  }
  // front_left_clearance
  if (lhs->front_left_clearance != rhs->front_left_clearance) {
    return false;
  }
  // front_right_clearance
  if (lhs->front_right_clearance != rhs->front_right_clearance) {
    return false;
  }
  // obstacle_blocked
  if (lhs->obstacle_blocked != rhs->obstacle_blocked) {
    return false;
  }
  return true;
}

bool
my_robot_description__msg__SafetyDebug__copy(
  const my_robot_description__msg__SafetyDebug * input,
  my_robot_description__msg__SafetyDebug * output)
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
  // cmd_linear
  output->cmd_linear = input->cmd_linear;
  // cmd_angular
  output->cmd_angular = input->cmd_angular;
  // target_linear_after_safety
  output->target_linear_after_safety = input->target_linear_after_safety;
  // target_angular_after_avoid
  output->target_angular_after_avoid = input->target_angular_after_avoid;
  // current_linear
  output->current_linear = input->current_linear;
  // current_angular
  output->current_angular = input->current_angular;
  // front_range
  output->front_range = input->front_range;
  // rear_range
  output->rear_range = input->rear_range;
  // front_left_range
  output->front_left_range = input->front_left_range;
  // front_right_range
  output->front_right_range = input->front_right_range;
  // front_clearance
  output->front_clearance = input->front_clearance;
  // rear_clearance
  output->rear_clearance = input->rear_clearance;
  // front_left_clearance
  output->front_left_clearance = input->front_left_clearance;
  // front_right_clearance
  output->front_right_clearance = input->front_right_clearance;
  // obstacle_blocked
  output->obstacle_blocked = input->obstacle_blocked;
  return true;
}

my_robot_description__msg__SafetyDebug *
my_robot_description__msg__SafetyDebug__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_robot_description__msg__SafetyDebug * msg = (my_robot_description__msg__SafetyDebug *)allocator.allocate(sizeof(my_robot_description__msg__SafetyDebug), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(my_robot_description__msg__SafetyDebug));
  bool success = my_robot_description__msg__SafetyDebug__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
my_robot_description__msg__SafetyDebug__destroy(my_robot_description__msg__SafetyDebug * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    my_robot_description__msg__SafetyDebug__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
my_robot_description__msg__SafetyDebug__Sequence__init(my_robot_description__msg__SafetyDebug__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_robot_description__msg__SafetyDebug * data = NULL;

  if (size) {
    data = (my_robot_description__msg__SafetyDebug *)allocator.zero_allocate(size, sizeof(my_robot_description__msg__SafetyDebug), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = my_robot_description__msg__SafetyDebug__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        my_robot_description__msg__SafetyDebug__fini(&data[i - 1]);
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
my_robot_description__msg__SafetyDebug__Sequence__fini(my_robot_description__msg__SafetyDebug__Sequence * array)
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
      my_robot_description__msg__SafetyDebug__fini(&array->data[i]);
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

my_robot_description__msg__SafetyDebug__Sequence *
my_robot_description__msg__SafetyDebug__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_robot_description__msg__SafetyDebug__Sequence * array = (my_robot_description__msg__SafetyDebug__Sequence *)allocator.allocate(sizeof(my_robot_description__msg__SafetyDebug__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = my_robot_description__msg__SafetyDebug__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
my_robot_description__msg__SafetyDebug__Sequence__destroy(my_robot_description__msg__SafetyDebug__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    my_robot_description__msg__SafetyDebug__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
my_robot_description__msg__SafetyDebug__Sequence__are_equal(const my_robot_description__msg__SafetyDebug__Sequence * lhs, const my_robot_description__msg__SafetyDebug__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!my_robot_description__msg__SafetyDebug__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
my_robot_description__msg__SafetyDebug__Sequence__copy(
  const my_robot_description__msg__SafetyDebug__Sequence * input,
  my_robot_description__msg__SafetyDebug__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(my_robot_description__msg__SafetyDebug);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    my_robot_description__msg__SafetyDebug * data =
      (my_robot_description__msg__SafetyDebug *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!my_robot_description__msg__SafetyDebug__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          my_robot_description__msg__SafetyDebug__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!my_robot_description__msg__SafetyDebug__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
