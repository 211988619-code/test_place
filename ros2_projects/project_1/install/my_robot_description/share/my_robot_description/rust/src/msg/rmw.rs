#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "my_robot_description__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__my_robot_description__msg__SafetyDebug() -> *const std::ffi::c_void;
}

#[link(name = "my_robot_description__rosidl_generator_c")]
extern "C" {
    fn my_robot_description__msg__SafetyDebug__init(msg: *mut SafetyDebug) -> bool;
    fn my_robot_description__msg__SafetyDebug__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SafetyDebug>, size: usize) -> bool;
    fn my_robot_description__msg__SafetyDebug__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SafetyDebug>);
    fn my_robot_description__msg__SafetyDebug__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SafetyDebug>, out_seq: *mut rosidl_runtime_rs::Sequence<SafetyDebug>) -> bool;
}

// Corresponds to my_robot_description__msg__SafetyDebug
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SafetyDebug {

    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::rmw::Time,


    // This member is not documented.
    #[allow(missing_docs)]
    pub cmd_linear: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub cmd_angular: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub target_linear_after_safety: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub target_angular_after_avoid: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub current_linear: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub current_angular: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub front_range: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub rear_range: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub front_left_range: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub front_right_range: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub front_clearance: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub rear_clearance: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub front_left_clearance: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub front_right_clearance: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub obstacle_blocked: bool,

}



impl Default for SafetyDebug {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !my_robot_description__msg__SafetyDebug__init(&mut msg as *mut _) {
        panic!("Call to my_robot_description__msg__SafetyDebug__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SafetyDebug {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { my_robot_description__msg__SafetyDebug__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { my_robot_description__msg__SafetyDebug__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { my_robot_description__msg__SafetyDebug__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SafetyDebug {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SafetyDebug where Self: Sized {
  const TYPE_NAME: &'static str = "my_robot_description/msg/SafetyDebug";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__my_robot_description__msg__SafetyDebug() }
  }
}


#[link(name = "my_robot_description__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__my_robot_description__msg__WallFollowDebug() -> *const std::ffi::c_void;
}

#[link(name = "my_robot_description__rosidl_generator_c")]
extern "C" {
    fn my_robot_description__msg__WallFollowDebug__init(msg: *mut WallFollowDebug) -> bool;
    fn my_robot_description__msg__WallFollowDebug__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<WallFollowDebug>, size: usize) -> bool;
    fn my_robot_description__msg__WallFollowDebug__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<WallFollowDebug>);
    fn my_robot_description__msg__WallFollowDebug__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<WallFollowDebug>, out_seq: *mut rosidl_runtime_rs::Sequence<WallFollowDebug>) -> bool;
}

// Corresponds to my_robot_description__msg__WallFollowDebug
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct WallFollowDebug {

    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::rmw::Time,


    // This member is not documented.
    #[allow(missing_docs)]
    pub state: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub front_range: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub side_range: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub diagonal_range: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub distance_error: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub wall_angle_error: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub front_speed_scale: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub linear_command: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub angular_command: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub front_blocked: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub wall_lost: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub in_acquire_mode: bool,

}



impl Default for WallFollowDebug {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !my_robot_description__msg__WallFollowDebug__init(&mut msg as *mut _) {
        panic!("Call to my_robot_description__msg__WallFollowDebug__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for WallFollowDebug {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { my_robot_description__msg__WallFollowDebug__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { my_robot_description__msg__WallFollowDebug__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { my_robot_description__msg__WallFollowDebug__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for WallFollowDebug {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for WallFollowDebug where Self: Sized {
  const TYPE_NAME: &'static str = "my_robot_description/msg/WallFollowDebug";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__my_robot_description__msg__WallFollowDebug() }
  }
}


