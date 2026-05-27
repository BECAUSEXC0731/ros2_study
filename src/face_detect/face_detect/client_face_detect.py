
import rclpy
from rclpy.node import Node
from msg_interfaces.srv import FaceDetector
from cv_bridge import CvBridge
from ament_index_python.packages import get_package_share_directory
import cv2


class FaceDetectClient(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.bridge = CvBridge()
        self.default_image_path = get_package_share_directory('face_detect') + '/resource/image_face.png'
        self.client = self.create_client(FaceDetector, 'face_detect')
        self.image=cv2.imread(self.default_image_path)


    def send_request(self):
        #判断服务端是否在线
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('等待服务端的开启')
        request = FaceDetector.Request()
        request.image = self.bridge.cv2_to_imgmsg(self.image, encoding='bgr8')
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

      
        self.get_logger().info('接受到响应...一共又%d个目标,耗时%d ms'%(future.result().number, future.result().usetime)   )
       
        return future.result()





def main(args=None):
    rclpy.init(args=args)
    node = FaceDetectClient('face_detect_client')
    node.send_request()
    rclpy.spin(node)
    rclpy.shutdown()