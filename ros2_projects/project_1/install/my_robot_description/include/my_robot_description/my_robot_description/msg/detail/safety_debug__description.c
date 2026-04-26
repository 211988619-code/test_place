// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from my_robot_description:msg/SafetyDebug.idl
// generated code does not contain a copyright notice

#include "my_robot_description/msg/detail/safety_debug__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_my_robot_description
const rosidl_type_hash_t *
my_robot_description__msg__SafetyDebug__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xf6, 0xfb, 0x7a, 0x10, 0xdf, 0x7f, 0x57, 0xe7,
      0xbb, 0x7e, 0x79, 0xa7, 0x93, 0xf1, 0xda, 0x1a,
      0xd1, 0x0d, 0xd1, 0x5c, 0x27, 0x07, 0xdf, 0x49,
      0xe2, 0xd5, 0x18, 0x45, 0x15, 0x7c, 0xf1, 0x2a,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
#endif

static char my_robot_description__msg__SafetyDebug__TYPE_NAME[] = "my_robot_description/msg/SafetyDebug";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";

// Define type names, field names, and default values
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__stamp[] = "stamp";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__cmd_linear[] = "cmd_linear";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__cmd_angular[] = "cmd_angular";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__target_linear_after_safety[] = "target_linear_after_safety";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__target_angular_after_avoid[] = "target_angular_after_avoid";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__current_linear[] = "current_linear";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__current_angular[] = "current_angular";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__front_range[] = "front_range";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__rear_range[] = "rear_range";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__front_left_range[] = "front_left_range";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__front_right_range[] = "front_right_range";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__front_clearance[] = "front_clearance";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__rear_clearance[] = "rear_clearance";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__front_left_clearance[] = "front_left_clearance";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__front_right_clearance[] = "front_right_clearance";
static char my_robot_description__msg__SafetyDebug__FIELD_NAME__obstacle_blocked[] = "obstacle_blocked";

static rosidl_runtime_c__type_description__Field my_robot_description__msg__SafetyDebug__FIELDS[] = {
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__stamp, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__cmd_linear, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__cmd_angular, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__target_linear_after_safety, 26, 26},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__target_angular_after_avoid, 26, 26},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__current_linear, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__current_angular, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__front_range, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__rear_range, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__front_left_range, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__front_right_range, 17, 17},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__front_clearance, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__rear_clearance, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__front_left_clearance, 20, 20},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__front_right_clearance, 21, 21},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__SafetyDebug__FIELD_NAME__obstacle_blocked, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription my_robot_description__msg__SafetyDebug__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
my_robot_description__msg__SafetyDebug__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {my_robot_description__msg__SafetyDebug__TYPE_NAME, 36, 36},
      {my_robot_description__msg__SafetyDebug__FIELDS, 16, 16},
    },
    {my_robot_description__msg__SafetyDebug__REFERENCED_TYPE_DESCRIPTIONS, 1, 1},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "builtin_interfaces/Time stamp\n"
  "float32 cmd_linear\n"
  "float32 cmd_angular\n"
  "float32 target_linear_after_safety\n"
  "float32 target_angular_after_avoid\n"
  "float32 current_linear\n"
  "float32 current_angular\n"
  "float32 front_range\n"
  "float32 rear_range\n"
  "float32 front_left_range\n"
  "float32 front_right_range\n"
  "float32 front_clearance\n"
  "float32 rear_clearance\n"
  "float32 front_left_clearance\n"
  "float32 front_right_clearance\n"
  "bool obstacle_blocked";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
my_robot_description__msg__SafetyDebug__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {my_robot_description__msg__SafetyDebug__TYPE_NAME, 36, 36},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 404, 404},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
my_robot_description__msg__SafetyDebug__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[2];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 2, 2};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *my_robot_description__msg__SafetyDebug__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
