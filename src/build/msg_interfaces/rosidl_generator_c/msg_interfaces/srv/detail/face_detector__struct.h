// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from msg_interfaces:srv/FaceDetector.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__SRV__DETAIL__FACE_DETECTOR__STRUCT_H_
#define MSG_INTERFACES__SRV__DETAIL__FACE_DETECTOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'image'
#include "sensor_msgs/msg/detail/image__struct.h"

/// Struct defined in srv/FaceDetector in the package msg_interfaces.
typedef struct msg_interfaces__srv__FaceDetector_Request
{
  sensor_msgs__msg__Image image;
} msg_interfaces__srv__FaceDetector_Request;

// Struct for a sequence of msg_interfaces__srv__FaceDetector_Request.
typedef struct msg_interfaces__srv__FaceDetector_Request__Sequence
{
  msg_interfaces__srv__FaceDetector_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_interfaces__srv__FaceDetector_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'top'
// Member 'left'
// Member 'right'
// Member 'bottom'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/FaceDetector in the package msg_interfaces.
typedef struct msg_interfaces__srv__FaceDetector_Response
{
  int16_t number;
  float usetime;
  rosidl_runtime_c__float__Sequence top;
  rosidl_runtime_c__float__Sequence left;
  rosidl_runtime_c__float__Sequence right;
  rosidl_runtime_c__float__Sequence bottom;
} msg_interfaces__srv__FaceDetector_Response;

// Struct for a sequence of msg_interfaces__srv__FaceDetector_Response.
typedef struct msg_interfaces__srv__FaceDetector_Response__Sequence
{
  msg_interfaces__srv__FaceDetector_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_interfaces__srv__FaceDetector_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MSG_INTERFACES__SRV__DETAIL__FACE_DETECTOR__STRUCT_H_
