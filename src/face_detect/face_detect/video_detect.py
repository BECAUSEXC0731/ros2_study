# face_detect/face_detect/video_detect.py
import rclpy
from rclpy.node import Node
from msg_interfaces.srv import FaceDetector
from cv_bridge import CvBridge
from ament_index_python.packages import get_package_share_directory
import cv2
import os
import sys
try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                                QPushButton, QVBoxLayout, QWidget, QHBoxLayout,
                                QFileDialog, QMessageBox)
    from PyQt5.QtGui import QImage, QPixmap
    from PyQt5.QtCore import QTimer
    Qt = __import__('PyQt5.QtCore', fromlist=['Qt']).Qt
    QT_AVAILABLE = True
except ImportError:
    try:
        from PySide2.QtWidgets import (QApplication, QMainWindow, QLabel, 
                                      QPushButton, QVBoxLayout, QWidget, QHBoxLayout,
                                      QFileDialog, QMessageBox)
        from PySide2.QtGui import QImage, QPixmap
        from PySide2.QtCore import QTimer
        Qt = __import__('PySide2.QtCore', fromlist=['Qt']).Qt
        QT_AVAILABLE = True
    except ImportError:
        QT_AVAILABLE = False
        print("PyQt5 or PySide2 not available. Please install one of them.")


class FaceDetectClient(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.bridge = CvBridge()
        self.client = self.create_client(FaceDetector, 'face_detect')
        
        # WSL2兼容的摄像头初始化 - 尝试多种方式
        self.cap = None
        self.camera_available = False
        
        # 尝试不同参数打开摄像头
        camera_options = [
            (0, cv2.CAP_V4L2),
            (1, cv2.CAP_V4L2),
            ('/dev/video0', cv2.CAP_V4L2),
            ('/dev/video1', cv2.CAP_V4L2),
            0,
            1,
        ]
        
        for option in camera_options:
            try:
                if isinstance(option, tuple):
                    idx, api = option
                    self.cap = cv2.VideoCapture(idx, api)
                else:
                    self.cap = cv2.VideoCapture(option)
                
                if self.cap.isOpened():
                    # 尝试读取一帧确认摄像头工作
                    ret, test_frame = self.cap.read()
                    if ret:
                        self.get_logger().info(f'成功打开摄像头，使用选项: {option}')
                        self.camera_available = True
                        
                        # 设置摄像头属性以优化性能
                        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                        self.cap.set(cv2.CAP_PROP_FPS, 30)
                        
                        break
                    else:
                        self.get_logger().warn(f'摄像头选项 {option} 打开但无法读取帧')
                        self.cap.release()
                        self.cap = None
                else:
                    self.get_logger().debug(f'摄像头选项 {option} 无法打开')
                    
            except Exception as e:
                self.get_logger().warn(f'摄像头选项 {option} 出错: {str(e)}')
        
        if not self.camera_available:
            self.get_logger().warn('所有摄像头选项都失败，将在GUI中提供替代选项')
        
        # 加载默认图片（如果有）
        self.default_image = None
        try:
            pkg_share = get_package_share_directory('face_detect')
            default_image_path = os.path.join(pkg_share, 'resource', 'image_face.png')
            if os.path.exists(default_image_path):
                self.default_image = cv2.imread(default_image_path)
                if self.default_image is not None:
                    self.get_logger().info(f'加载默认图片: {default_image_path}')
        except Exception as e:
            self.get_logger().warn(f'无法加载默认图片: {str(e)}')

    def detect_faces(self, image):
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('等待服务端的开启')
        
        request = FaceDetector.Request()
        request.image = self.bridge.cv2_to_imgmsg(image, encoding='bgr8')
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        
        if future.result() is not None:
            result = future.result()
            self.get_logger().info('接收到响应...一共%d个目标,耗时%.2f ms' % (result.number, result.usetime * 1000))
            return result
        else:
            self.get_logger().error('服务调用失败')
            return None

    def read_camera_frame(self):
        if self.camera_available and self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return frame
            else:
                self.get_logger().warn('无法从摄像头读取帧')
        return None

    def detect_on_image(self, image_path):
        """对指定路径的图片进行人脸检测"""
        image = cv2.imread(image_path)
        if image is not None:
            return self.detect_faces(image)
        return None

    def destroy_node(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()
        super().destroy_node()


def main(args=None):
    if not QT_AVAILABLE:
        print("No Qt library available!")
        return
        
    rclpy.init(args=args)
    node = FaceDetectClient('face_detect_client')
    
    app = QApplication(sys.argv)
    
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.node = node
            self.detection_active = False
            self.current_image = None
            
            self.setWindowTitle("人脸检测系统 (WSL2兼容)")
            self.setGeometry(100, 100, 900, 700)
            
            central_widget = QWidget()
            self.setCentralWidget(central_widget)
            layout = QVBoxLayout(central_widget)
            
            # 图像显示区域
            self.image_label = QLabel()
            self.image_label.setAlignment(Qt.AlignCenter)
            self.image_label.setMinimumSize(640, 480)
            self.image_label.setStyleSheet("border: 1px solid gray;")
            layout.addWidget(self.image_label)
            
            # 按钮布局
            button_layout = QHBoxLayout()
            
            self.start_cam_button = QPushButton("开启摄像头")
            self.start_cam_button.setEnabled(node.camera_available)
            self.start_cam_button.clicked.connect(self.start_camera_detection)
            
            self.stop_cam_button = QPushButton("停止摄像头")
            self.stop_cam_button.setEnabled(False)
            self.stop_cam_button.clicked.connect(self.stop_camera_detection)
            
            self.load_image_button = QPushButton("加载图片")
            self.load_image_button.clicked.connect(self.load_image)
            
            self.detect_loaded_button = QPushButton("检测加载的图片")
            self.detect_loaded_button.clicked.connect(self.detect_loaded_image)
            
            button_layout.addWidget(self.start_cam_button)
            button_layout.addWidget(self.stop_cam_button)
            button_layout.addWidget(self.load_image_button)
            button_layout.addWidget(self.detect_loaded_button)
            layout.addLayout(button_layout)
            
            # 状态标签
            self.status_label = QLabel("状态: 系统就绪")
            layout.addWidget(self.status_label)
            
            # 摄像头检测定时器
            self.cam_timer = QTimer()
            self.cam_timer.timeout.connect(self.update_camera_frame)
            
            # 如果有默认图片，显示它
            if node.default_image is not None:
                self.display_cv2_image(node.default_image)
                self.status_label.setText("状态: 显示默认图片")

        def start_camera_detection(self):
            if self.node.camera_available:
                self.detection_active = True
                self.cam_timer.start(50)  # 20fps
                self.start_cam_button.setEnabled(False)
                self.stop_cam_button.setEnabled(True)
                self.status_label.setText("状态: 摄像头检测中...")
            else:
                QMessageBox.warning(self, "警告", "摄像头不可用！请使用图片检测功能。")

        def stop_camera_detection(self):
            self.detection_active = False
            self.cam_timer.stop()
            self.start_cam_button.setEnabled(True)
            self.stop_cam_button.setEnabled(False)
            self.status_label.setText("状态: 摄像头已停止")

        def update_camera_frame(self):
            if not self.detection_active:
                return
                
            frame = self.node.read_camera_frame()
            if frame is not None:
                # 对当前帧进行人脸检测
                result = self.node.detect_faces(frame)
                if result is not None:
                    # 在图像上绘制检测结果
                    for i in range(result.number):
                        left = int(result.left[i])
                        top = int(result.top[i])
                        right = int(result.right[i])
                        bottom = int(result.bottom[i])
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                
                self.display_cv2_image(frame)
            else:
                # 如果无法读取摄像头帧，显示状态信息
                self.status_label.setText("状态: 无法从摄像头读取帧")

        def load_image(self):
            file_path, _ = QFileDialog.getOpenFileName(
                self, "选择图片", "", "图片文件 (*.png *.jpg *.jpeg *.bmp)"
            )
            if file_path:
                self.loaded_image_path = file_path
                image = cv2.imread(file_path)
                if image is not None:
                    self.display_cv2_image(image)
                    self.current_image = image
                    self.status_label.setText(f"状态: 已加载图片 {os.path.basename(file_path)}")
                else:
                    QMessageBox.critical(self, "错误", "无法加载选定的图片！")

        def detect_loaded_image(self):
            if hasattr(self, 'loaded_image_path') and os.path.exists(self.loaded_image_path):
                result = self.node.detect_on_image(self.loaded_image_path)
                if result is not None:
                    # 重新加载图片并在其上绘制检测结果
                    image = cv2.imread(self.loaded_image_path)
                    for i in range(result.number):
                        left = int(result.left[i])
                        top = int(result.top[i])
                        right = int(result.right[i])
                        bottom = int(result.bottom[i])
                        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
                    
                    self.display_cv2_image(image)
                    self.status_label.setText(f"状态: 检测完成，找到 {result.number} 个人脸")
            else:
                QMessageBox.warning(self, "警告", "请先加载一张图片！")

        def display_cv2_image(self, cv2_image):
            """显示OpenCV图像"""
            rgb_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            self.image_label.setPixmap(pixmap.scaled(640, 480, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    window = MainWindow()
    window.show()
    
    try:
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()