import sys
import rclpy
from rclpy.node import Node
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QHBoxLayout
)
from PySide6.QtCore import QTimer, Qt
from msg_interfaces.msg import SystemStatus   


class StutsSubNode(Node):
    """ROS 2 订阅者节点，接收 system_status 消息"""
    def __init__(self):
        super().__init__('stuts_subscriber')
        self.subscription = self.create_subscription(
            SystemStatus,
            'system_status',
            self.status_callback,
            10
        )
        self.current_status = None   # 保存最新消息，供 UI 读取

    def status_callback(self, msg):
        """收到消息时的回调（运行在主线程，由 QTimer 触发的 spin_once 调用）"""
        self.current_status = msg
        # 注意：这里可以直接更新 UI，因为是在主线程中执行
        # 但我们让 UI 主动读取 self.current_status，耦合更低

class MainWindow(QWidget):
    def __init__(self, ros_node: StutsSubNode):
        super().__init__()
        self.ros_node = ros_node
        self.setWindowTitle("系统状态监视器")
        self.resize(400, 300)          # 可调整大小，初始宽度400高度300
        self.setMinimumSize(300, 250)  # 限制最小尺寸，防止内容被裁剪

        # 创建布局
        layout = QVBoxLayout(self)

        # 主机名
        self.host_label = QLabel("主机名: --")
        layout.addWidget(self.host_label)

        # CPU 使用率
        self.cpu_label = QLabel("CPU 使用率: -- %")
        layout.addWidget(self.cpu_label)

        # 内存使用率
        self.mem_percent_label = QLabel("内存使用率: -- %")
        layout.addWidget(self.mem_percent_label)

        # 可用内存
        self.mem_avail_label = QLabel("可用内存: -- MB")
        layout.addWidget(self.mem_avail_label)

        # 网络发送总量
        self.net_sent_label = QLabel("网卡发送: -- MB")
        layout.addWidget(self.net_sent_label)

        # 网络接收总量
        self.net_recv_label = QLabel("网卡接收: -- MB")
        layout.addWidget(self.net_recv_label)

        # 时间戳
        self.time_label = QLabel("最后更新: --")
        layout.addWidget(self.time_label)

        # 退出按钮
        btn_layout = QHBoxLayout()
        quit_btn = QPushButton("退出")
        quit_btn.clicked.connect(self.close)
        btn_layout.addStretch()
        btn_layout.addWidget(quit_btn)
        layout.addLayout(btn_layout)

        # 可选：设置拉伸因子，让所有信息标签随窗口缩放均匀伸展，按钮行不伸展
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget() and item.widget() != quit_btn:
                layout.setStretchFactor(item.widget(), 1)
        layout.setStretchFactor(btn_layout, 0)  # 按钮行不拉伸

        # 启动定时器，每 100ms 从 ROS 节点获取最新数据并刷新 UI
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(100)

    def update_ui(self):
        """从 ROS 节点读取最新消息，更新界面标签"""
        msg = self.ros_node.current_status
        if msg is None:
            return

        self.host_label.setText(f"主机名: {msg.host_name}")
        self.cpu_label.setText(f"CPU 使用率: {msg.cpu_percent:.1f} %")
        self.mem_percent_label.setText(f"内存使用率: {msg.memory_percent:.1f} %")
        self.mem_avail_label.setText(f"可用内存: {msg.memory_available:.1f} MB")
        self.net_sent_label.setText(f"网卡发送: {msg.net_sent:.2f} MB")
        self.net_recv_label.setText(f"网卡接收: {msg.net_recv:.2f} MB")
        stamp_sec = msg.stamp.sec + msg.stamp.nanosec * 1e-9
        self.time_label.setText(f"最后更新: {stamp_sec:.3f} 秒")

    def closeEvent(self, event):
        self.timer.stop()
        rclpy.shutdown()
        event.accept()
def main(args=None):
    rclpy.init(args=args)

    # 创建 ROS 订阅节点
    ros_node = StutsSubNode()

    # 创建 Qt 应用
    qt_app = QApplication(sys.argv)
    window = MainWindow(ros_node)
    window.show()

    # 关键：用 QTimer 驱动 ROS 事件循环（每 50ms 处理一次）
    # 这样 ROS 回调就会在 Qt 主线程中执行，可以安全更新 UI
    ros_timer = QTimer()
    ros_timer.timeout.connect(lambda: rclpy.spin_once(ros_node, timeout_sec=0))
    ros_timer.start(50)

    # 进入 Qt 事件循环
    exit_code = qt_app.exec()

    # 清理
    ros_timer.stop()
    ros_node.destroy_node()
    rclpy.shutdown()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()