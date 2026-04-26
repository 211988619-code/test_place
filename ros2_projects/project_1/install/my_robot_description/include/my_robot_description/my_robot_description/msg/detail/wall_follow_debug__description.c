// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from my_robot_description:msg/WallFollowDebug.idl
// generated code does not contain a copyright notice

#include "my_robot_description/msg/detail/wall_follow_debug__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_my_robot_description
const rosidl_type_hash_t *
my_robot_description__msg__WallFollowDebug__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x64, 0x94, 0xf4, 0x78, 0x6d, 0x19, 0x81, 0x81,
      0xf8, 0xe3, 0xbf, 0xae, 0x82, 0x2c, 0x41, 0xde,
      0xa9, 0x41, 0x25, 0x4c, 0x60, 0xf1, 0xd7, 0xe3,
      0x5b, 0x97, 0xe6, 0xb9, 0xf2, 0xc6, 0xd9, 0xbf,
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

static char my_robot_description__msg__WallFollowDebug__TYPE_NAME[] = "my_robot_description/msg/WallFollowDebug";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";

// Define type names, field names, and default values
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__stamp[] = "stamp";
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__state[] = "state";
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__front_range[] = "front_range";
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__side_range[] = "side_range";
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__diagonal_range[] = "diagonal_range";
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__distance_error[] = "distance_error";
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__wall_angle_error[] = "wall_angle_error";
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__front_speed_scale[] = "front_speed_scale";
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__linear_command[] = "linear_command";
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__angular_command[] = "angular_command";
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__front_blocked[] = "front_blocked";
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__wall_lost[] = "wall_lost";
static char my_robot_description__msg__WallFollowDebug__FIELD_NAME__in_acquire_mode[] = "in_acquire_mode";

static rosidl_runtime_c__type_description__Field my_robot_description__msg__WallFollowDebug__FIELDS[] = {
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__stamp, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__state, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__front_range, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__side_range, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__diagonal_range, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__distance_error, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__wall_angle_error, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__front_speed_scale, 17, 17},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__linear_command, 14, 14},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__angular_command, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__front_blocked, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__wall_lost, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {my_robot_description__msg__WallFollowDebug__FIELD_NAME__in_acquire_mode, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription my_robot_description__msg__WallFollowDebug__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
my_robot_description__msg__WallFollowDebug__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {my_robot_description__msg__WallFollowDebug__TYPE_NAME, 40, 40},
      {my_robot_description__msg__WallFollowDebug__FIELDS, 13, 13},
    },
    {my_robot_description__msg__WallFollowDebug__REFERENCED_TYPE_DESCRIPTIONS, 1, 1},
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
  "string state\n"
  "float32 front_range\n"
  "float32 side_range\n"
  "float32 diagonal_range\n"
  "float32 distance_error\n"
  "float32 wall_angle_error\n"
  "float32 front_speed_scale\n"
  "float32 linear_command\n"
  "float32 angular_command\n"
  "bool front_blocked\n"
  "bool wall_lost\n"
  "bool in_acquire_mode";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
my_robot_description__msg__WallFollowDebug__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {my_robot_description__msg__WallFollowDebug__TYPE_NAME, 40, 40},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 281, 281},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
my_robot_description__msg__WallFollowDebug__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[2];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 2, 2};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *my_robot_description__msg__WallFollowDebug__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
