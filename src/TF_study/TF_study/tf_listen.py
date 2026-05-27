import rclpy
from rclpy.node import Node
from tf2_ros import TransformListener,Buffer
from geometry_msgs.msg import TransformStamped
from tf_transformations import euler_from_quaternion
import math




class TfBroadListen(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.buffer = Buffer()
        self.listener = TransformListener(self.buffer,node=self)#顺序不能错
        
   
        self.timer = self.create_timer(1.0, self.get_tf)
     

         
 
    def get_tf(self):
        
        try:
            result=self.buffer.lookup_transform('base_link','camera_link',rclpy.time.Time())
            transform=result.transform
            self.get_logger().info('平移：x={:.2f},y={:.2f},z={:.2f}'.format(transform.translation.x,transform.translation.y,transform.translation.z))
            self.get_logger().info('旋转：x={:.2f},y={:.2f},z={:.2f},w={:.2f}'.format(transform.rotation.x,transform.rotation.y,transform.rotation.z,transform.rotation.w))
            euler=euler_from_quaternion([transform.rotation.x,transform.rotation.y,transform.rotation.z,transform.rotation.w])
            self.get_logger().info('旋转RPY：roll={:.2f},pitch={:.2f},yaw={:.2f}'.format(euler[0],euler[1],euler[2]))
        except Exception as e:
            self.get_logger().info('没有找到TF变换...')


 

def main(args=None):
    rclpy.init(args=args)
    node = TfBroadListen('tf_broad_listen')
    rclpy.spin(node)
    rclpy.shutdown()
