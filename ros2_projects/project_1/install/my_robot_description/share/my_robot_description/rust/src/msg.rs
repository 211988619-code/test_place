#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to my_robot_description__msg__SafetyDebug

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SafetyDebug {

    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::Time,


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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::SafetyDebug::default())
  }
}

impl rosidl_runtime_rs::Message for SafetyDebug {
  type RmwMsg = super::msg::rmw::SafetyDebug;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        stamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Owned(msg.stamp)).into_owned(),
        cmd_linear: msg.cmd_linear,
        cmd_angular: msg.cmd_angular,
        target_linear_after_safety: msg.target_linear_after_safety,
        target_angular_after_avoid: msg.target_angular_after_avoid,
        current_linear: msg.current_linear,
        current_angular: msg.current_angular,
        front_range: msg.front_range,
        rear_range: msg.rear_range,
        front_left_range: msg.front_left_range,
        front_right_range: msg.front_right_range,
        front_clearance: msg.front_clearance,
        rear_clearance: msg.rear_clearance,
        front_left_clearance: msg.front_left_clearance,
        front_right_clearance: msg.front_right_clearance,
        obstacle_blocked: msg.obstacle_blocked,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        stamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Borrowed(&msg.stamp)).into_owned(),
      cmd_linear: msg.cmd_linear,
      cmd_angular: msg.cmd_angular,
      target_linear_after_safety: msg.target_linear_after_safety,
      target_angular_after_avoid: msg.target_angular_after_avoid,
      current_linear: msg.current_linear,
      current_angular: msg.current_angular,
      front_range: msg.front_range,
      rear_range: msg.rear_range,
      front_left_range: msg.front_left_range,
      front_right_range: msg.front_right_range,
      front_clearance: msg.front_clearance,
      rear_clearance: msg.rear_clearance,
      front_left_clearance: msg.front_left_clearance,
      front_right_clearance: msg.front_right_clearance,
      obstacle_blocked: msg.obstacle_blocked,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      stamp: builtin_interfaces::msg::Time::from_rmw_message(msg.stamp),
      cmd_linear: msg.cmd_linear,
      cmd_angular: msg.cmd_angular,
      target_linear_after_safety: msg.target_linear_after_safety,
      target_angular_after_avoid: msg.target_angular_after_avoid,
      current_linear: msg.current_linear,
      current_angular: msg.current_angular,
      front_range: msg.front_range,
      rear_range: msg.rear_range,
      front_left_range: msg.front_left_range,
      front_right_range: msg.front_right_range,
      front_clearance: msg.front_clearance,
      rear_clearance: msg.rear_clearance,
      front_left_clearance: msg.front_left_clearance,
      front_right_clearance: msg.front_right_clearance,
      obstacle_blocked: msg.obstacle_blocked,
    }
  }
}


// Corresponds to my_robot_description__msg__WallFollowDebug

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct WallFollowDebug {

    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::Time,


    // This member is not documented.
    #[allow(missing_docs)]
    pub state: std::string::String,


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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::WallFollowDebug::default())
  }
}

impl rosidl_runtime_rs::Message for WallFollowDebug {
  type RmwMsg = super::msg::rmw::WallFollowDebug;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        stamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Owned(msg.stamp)).into_owned(),
        state: msg.state.as_str().into(),
        front_range: msg.front_range,
        side_range: msg.side_range,
        diagonal_range: msg.diagonal_range,
        distance_error: msg.distance_error,
        wall_angle_error: msg.wall_angle_error,
        front_speed_scale: msg.front_speed_scale,
        linear_command: msg.linear_command,
        angular_command: msg.angular_command,
        front_blocked: msg.front_blocked,
        wall_lost: msg.wall_lost,
        in_acquire_mode: msg.in_acquire_mode,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        stamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Borrowed(&msg.stamp)).into_owned(),
        state: msg.state.as_str().into(),
      front_range: msg.front_range,
      side_range: msg.side_range,
      diagonal_range: msg.diagonal_range,
      distance_error: msg.distance_error,
      wall_angle_error: msg.wall_angle_error,
      front_speed_scale: msg.front_speed_scale,
      linear_command: msg.linear_command,
      angular_command: msg.angular_command,
      front_blocked: msg.front_blocked,
      wall_lost: msg.wall_lost,
      in_acquire_mode: msg.in_acquire_mode,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      stamp: builtin_interfaces::msg::Time::from_rmw_message(msg.stamp),
      state: msg.state.to_string(),
      front_range: msg.front_range,
      side_range: msg.side_range,
      diagonal_range: msg.diagonal_range,
      distance_error: msg.distance_error,
      wall_angle_error: msg.wall_angle_error,
      front_speed_scale: msg.front_speed_scale,
      linear_command: msg.linear_command,
      angular_command: msg.angular_command,
      front_blocked: msg.front_blocked,
      wall_lost: msg.wall_lost,
      in_acquire_mode: msg.in_acquire_mode,
    }
  }
}


