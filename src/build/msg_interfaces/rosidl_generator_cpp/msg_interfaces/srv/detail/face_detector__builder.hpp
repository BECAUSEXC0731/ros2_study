// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from msg_interfaces:srv/FaceDetector.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__FACE_DETECTOR__BUILDER_HPP_
#define MSG_INTERFACES__SRV__DETAIL__FACE_DETECTOR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "msg_interfaces/srv/detail/face_detector__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace msg_interfaces
{

namespace srv
{

namespace builder
{

class Init_FaceDetector_Request_image
{
public:
  Init_FaceDetector_Request_image()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::msg_interfaces::srv::FaceDetector_Request image(::msg_interfaces::srv::FaceDetector_Request::_image_type arg)
  {
    msg_.image = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_interfaces::srv::FaceDetector_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_interfaces::srv::FaceDetector_Request>()
{
  return msg_interfaces::srv::builder::Init_FaceDetector_Request_image();
}

}  // namespace msg_interfaces


namespace msg_interfaces
{

namespace srv
{

namespace builder
{

class Init_FaceDetector_Response_bottom
{
public:
  explicit Init_FaceDetector_Response_bottom(::msg_interfaces::srv::FaceDetector_Response & msg)
  : msg_(msg)
  {}
  ::msg_interfaces::srv::FaceDetector_Response bottom(::msg_interfaces::srv::FaceDetector_Response::_bottom_type arg)
  {
    msg_.bottom = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_interfaces::srv::FaceDetector_Response msg_;
};

class Init_FaceDetector_Response_right
{
public:
  explicit Init_FaceDetector_Response_right(::msg_interfaces::srv::FaceDetector_Response & msg)
  : msg_(msg)
  {}
  Init_FaceDetector_Response_bottom right(::msg_interfaces::srv::FaceDetector_Response::_right_type arg)
  {
    msg_.right = std::move(arg);
    return Init_FaceDetector_Response_bottom(msg_);
  }

private:
  ::msg_interfaces::srv::FaceDetector_Response msg_;
};

class Init_FaceDetector_Response_left
{
public:
  explicit Init_FaceDetector_Response_left(::msg_interfaces::srv::FaceDetector_Response & msg)
  : msg_(msg)
  {}
  Init_FaceDetector_Response_right left(::msg_interfaces::srv::FaceDetector_Response::_left_type arg)
  {
    msg_.left = std::move(arg);
    return Init_FaceDetector_Response_right(msg_);
  }

private:
  ::msg_interfaces::srv::FaceDetector_Response msg_;
};

class Init_FaceDetector_Response_top
{
public:
  explicit Init_FaceDetector_Response_top(::msg_interfaces::srv::FaceDetector_Response & msg)
  : msg_(msg)
  {}
  Init_FaceDetector_Response_left top(::msg_interfaces::srv::FaceDetector_Response::_top_type arg)
  {
    msg_.top = std::move(arg);
    return Init_FaceDetector_Response_left(msg_);
  }

private:
  ::msg_interfaces::srv::FaceDetector_Response msg_;
};

class Init_FaceDetector_Response_usetime
{
public:
  explicit Init_FaceDetector_Response_usetime(::msg_interfaces::srv::FaceDetector_Response & msg)
  : msg_(msg)
  {}
  Init_FaceDetector_Response_top usetime(::msg_interfaces::srv::FaceDetector_Response::_usetime_type arg)
  {
    msg_.usetime = std::move(arg);
    return Init_FaceDetector_Response_top(msg_);
  }

private:
  ::msg_interfaces::srv::FaceDetector_Response msg_;
};

class Init_FaceDetector_Response_number
{
public:
  Init_FaceDetector_Response_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FaceDetector_Response_usetime number(::msg_interfaces::srv::FaceDetector_Response::_number_type arg)
  {
    msg_.number = std::move(arg);
    return Init_FaceDetector_Response_usetime(msg_);
  }

private:
  ::msg_interfaces::srv::FaceDetector_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_interfaces::srv::FaceDetector_Response>()
{
  return msg_interfaces::srv::builder::Init_FaceDetector_Response_number();
}

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__SRV__DETAIL__FACE_DETECTOR__BUILDER_HPP_
