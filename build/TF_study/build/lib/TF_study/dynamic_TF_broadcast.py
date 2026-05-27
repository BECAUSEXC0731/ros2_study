import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
from tf_transformations import quaternion_from_euler
import math




class DynamicTFBroadcaster(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(1.0, self.broadcast_tf)
     

         
 
    def broadcast_tf(self):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'base_link'
        t.child_frame_id = 'camera_link'


        t.transform.translation.x = 0.5
        t.transform.translation.y = 0.3
        t.transform.translation.z = 0.6
        q = quaternion_from_euler(0,0,0)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        self.broadcaster.sendTransform(t)
        self.get_logger().info('发布动态TF变换...')




def main(args=None):
    rclpy.init(args=args)
    node = DynamicTFBroadcaster('dynamic_tf_broadcaster')
    rclpy.spin(node)
    rclpy.shutdown()
