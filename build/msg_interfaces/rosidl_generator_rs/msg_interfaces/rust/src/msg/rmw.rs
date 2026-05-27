#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "msg_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__msg_interfaces__msg__SystemStatus() -> *const std::ffi::c_void;
}

#[link(name = "msg_interfaces__rosidl_generator_c")]
extern "C" {
    fn msg_interfaces__msg__SystemStatus__init(msg: *mut SystemStatus) -> bool;
    fn msg_interfaces__msg__SystemStatus__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SystemStatus>, size: usize) -> bool;
    fn msg_interfaces__msg__SystemStatus__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SystemStatus>);
    fn msg_interfaces__msg__SystemStatus__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SystemStatus>, out_seq: *mut rosidl_runtime_rs::Sequence<SystemStatus>) -> bool;
}

// Corresponds to msg_interfaces__msg__SystemStatus
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SystemStatus {
    /// 记录时间戳( 原builtin_interfaces/msg/Time)被别的消息接口依赖需要去掉msg
    pub stamp: builtin_interfaces::msg::rmw::Time,

    /// 主机名字
    pub host_name: rosidl_runtime_rs::String,

    /// cpu占用率
    pub cpu_percent: f32,

    /// 内存占用率
    pub memory_percent: f32,

    /// 总内存
    pub memory_available: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub net_sent: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub net_recv: f64,

}



impl Default for SystemStatus {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !msg_interfaces__msg__SystemStatus__init(&mut msg as *mut _) {
        panic!("Call to msg_interfaces__msg__SystemStatus__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SystemStatus {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { msg_interfaces__msg__SystemStatus__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { msg_interfaces__msg__SystemStatus__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { msg_interfaces__msg__SystemStatus__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SystemStatus {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SystemStatus where Self: Sized {
  const TYPE_NAME: &'static str = "msg_interfaces/msg/SystemStatus";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__msg_interfaces__msg__SystemStatus() }
  }
}


