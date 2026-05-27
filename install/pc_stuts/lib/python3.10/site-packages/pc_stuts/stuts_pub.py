import rclpy
from rclpy.node import Node
from msg_interfaces.msg import SystemStatus
import psutil
import platform


class StutsPub(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.publisher_ = self.create_publisher(SystemStatus, 'system_status', 10)
        self.timer_=self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        cpu_percent=psutil.cpu_percent()
        memory_info=psutil.virtual_memory()
        net_io_counters=psutil.net_io_counters()

        msg=SystemStatus()
        msg.stamp=self.get_clock().now().to_msg()
        msg.host_name=platform.node()
        msg.cpu_percent=cpu_percent
        msg.memory_percent=memory_info.percent
        msg.memory_available=float(memory_info.available)
        msg.net_sent=net_io_counters.bytes_sent/1024/1024
        msg.net_recv=net_io_counters.bytes_recv/1024/1024
        

        self.get_logger().info("发布者正在发布数据...")
        self.publisher_.publish(msg)




def main():
    rclpy.init()
    stuts_pub = StutsPub("stuts_publisher")
    stuts_pub.get_logger().info("发布者已经启动！")
    rclpy.spin(stuts_pub)
    stuts_pub.destroy_node()
    rclpy.shutdown()