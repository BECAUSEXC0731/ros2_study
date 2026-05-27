// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from msg_interfaces:srv/FaceDetector.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__FACE_DETECTOR__STRUCT_HPP_
#define MSG_INTERFACES__SRV__DETAIL__FACE_DETECTOR__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'image'
#include "sensor_msgs/msg/detail/image__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__msg_interfaces__srv__FaceDetector_Request __attribute__((deprecated))
#else
# define DEPRECATED__msg_interfaces__srv__FaceDetector_Request __declspec(deprecated)
#endif

namespace msg_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct FaceDetector_Request_
{
  using Type = FaceDetector_Request_<ContainerAllocator>;

  explicit FaceDetector_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : image(_init)
  {
    (void)_init;
  }

  explicit FaceDetector_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : image(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _image_type =
    sensor_msgs::msg::Image_<ContainerAllocator>;
  _image_type image;

  // setters for named parameter idiom
  Type & set__image(
    const sensor_msgs::msg::Image_<ContainerAllocator> & _arg)
  {
    this->image = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    msg_interfaces::srv::FaceDetector_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const msg_interfaces::srv::FaceDetector_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<msg_interfaces::srv::FaceDetector_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<msg_interfaces::srv::FaceDetector_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::FaceDetector_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::FaceDetector_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::FaceDetector_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::FaceDetector_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<msg_interfaces::srv::FaceDetector_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<msg_interfaces::srv::FaceDetector_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__msg_interfaces__srv__FaceDetector_Request
    std::shared_ptr<msg_interfaces::srv::FaceDetector_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__msg_interfaces__srv__FaceDetector_Request
    std::shared_ptr<msg_interfaces::srv::FaceDetector_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FaceDetector_Request_ & other) const
  {
    if (this->image != other.image) {
      return false;
    }
    return true;
  }
  bool operator!=(const FaceDetector_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FaceDetector_Request_

// alias to use template instance with default allocator
using FaceDetector_Request =
  msg_interfaces::srv::FaceDetector_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace msg_interfaces


#ifndef _WIN32
# define DEPRECATED__msg_interfaces__srv__FaceDetector_Response __attribute__((deprecated))
#else
# define DEPRECATED__msg_interfaces__srv__FaceDetector_Response __declspec(deprecated)
#endif

namespace msg_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct FaceDetector_Response_
{
  using Type = FaceDetector_Response_<ContainerAllocator>;

  explicit FaceDetector_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->number = 0;
      this->usetime = 0.0f;
    }
  }

  explicit FaceDetector_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->number = 0;
      this->usetime = 0.0f;
    }
  }

  // field types and members
  using _number_type =
    int16_t;
  _number_type number;
  using _usetime_type =
    float;
  _usetime_type usetime;
  using _top_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _top_type top;
  using _left_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _left_type left;
  using _right_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _right_type right;
  using _bottom_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _bottom_type bottom;

  // setters for named parameter idiom
  Type & set__number(
    const int16_t & _arg)
  {
    this->number = _arg;
    return *this;
  }
  Type & set__usetime(
    const float & _arg)
  {
    this->usetime = _arg;
    return *this;
  }
  Type & set__top(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->top = _arg;
    return *this;
  }
  Type & set__left(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->left = _arg;
    return *this;
  }
  Type & set__right(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->right = _arg;
    return *this;
  }
  Type & set__bottom(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->bottom = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    msg_interfaces::srv::FaceDetector_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const msg_interfaces::srv::FaceDetector_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<msg_interfaces::srv::FaceDetector_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<msg_interfaces::srv::FaceDetector_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::FaceDetector_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::FaceDetector_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::srv::FaceDetector_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::srv::FaceDetector_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<msg_interfaces::srv::FaceDetector_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<msg_interfaces::srv::FaceDetector_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__msg_interfaces__srv__FaceDetector_Response
    std::shared_ptr<msg_interfaces::srv::FaceDetector_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__msg_interfaces__srv__FaceDetector_Response
    std::shared_ptr<msg_interfaces::srv::FaceDetector_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FaceDetector_Response_ & other) const
  {
    if (this->number != other.number) {
      return false;
    }
    if (this->usetime != other.usetime) {
      return false;
    }
    if (this->top != other.top) {
      return false;
    }
    if (this->left != other.left) {
      return false;
    }
    if (this->right != other.right) {
      return false;
    }
    if (this->bottom != other.bottom) {
      return false;
    }
    return true;
  }
  bool operator!=(const FaceDetector_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FaceDetector_Response_

// alias to use template instance with default allocator
using FaceDetector_Response =
  msg_interfaces::srv::FaceDetector_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace msg_interfaces

namespace msg_interfaces
{

namespace srv
{

struct FaceDetector
{
  using Request = msg_interfaces::srv::FaceDetector_Request;
  using Response = msg_interfaces::srv::FaceDetector_Response;
};

}  // namespace srv

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__SRV__DETAIL__FACE_DETECTOR__STRUCT_HPP_
