import face_recognition
import cv2
from ament_index_python.packages import get_package_share_directory  
import rclpy
from rclpy.node import Node
from msg_interfaces.srv import FaceDetector
from cv_bridge import CvBridge
import time
from rcl_interfaces.msg import SetParametersResult



class FaceDetect(Node): 
    def __init__(self,node_name):
        super().__init__(node_name)
        self.face_dec_srv = self.create_service(FaceDetector, 'face_detect', self.face_detect_callback)
        self.bridge = CvBridge()
        self.default_image_path = get_package_share_directory('face_detect') + '/resource/image_face.png'
        self.declare_parameter('number', 1)
        self.declare_parameter('model', 'hog')
        self.declare_parameter('log', '我的妈呀')
        self.number = self.get_parameter('number').value
        self.model = self.get_parameter('model').value
        self.log=self.get_parameter('log').value
        self.get_logger().info("服务启动成功")
        self.add_on_set_parameters_callback(self.parameter_callback)

    def parameter_callback(self, params):
        for param in params:
            if param.name == 'number' and param.type_ == rclpy.Parameter.Type.INTEGER:
                self.number = param.value
                self.get_logger().info(f"number参数已更新为: {self.number}")
            elif param.name == 'model' and param.type_ == rclpy.Parameter.Type.STRING:
                self.model = param.value
                self.get_logger().info(f"model参数已更新为: {self.model}")
            elif param.name == 'log' and param.type_ == rclpy.Parameter.Type.STRING:
                self.log = param.value
                self.get_logger().info(f"log参数已更新为: {self.log}")
        return SetParametersResult(successful=True)




    def face_detect_callback(self, request, response):
        if request.image.data:
            image = self.bridge.imgmsg_to_cv2(request.image, 'bgr8')
            

        else:
            image =cv2.imread(self.default_image_path)
            self.get_logger().info('使用默认图片')
        
        start_time=time.time()
        self.log=self.get_parameter('log').value
        self.get_logger().info('开始识别人脸')
        self.get_logger().warn(self.log)
        face_locations = face_recognition.face_locations(image, model=self.model, number_of_times_to_upsample=self.number)
        response.usetime = time.time() - start_time
        response.number = len(face_locations)
        for (top, right, bottom, left) in face_locations:
            response.top.append(top)
            response.right.append(right)
            response.bottom.append(bottom)
            response.left.append(left)
        
           
            

        return response
    


def main(args=None):

    rclpy.init(args=args)
    face_detect_node = FaceDetect('face_detect')
    rclpy.spin(face_detect_node)
    face_detect_node.destroy_node()
    rclpy.shutdown()
    
