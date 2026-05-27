import rclpy    
from rclpy.node import Node
from msg_interfaces.msg import SystemStatus



class StutsPub(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
      
        self.subscriber_ = self.create_subscription(SystemStatus, 'system_status', self.timer_callback, 10)
    

    def timer_callback(self, msg):
        self.get_logger().info('时间:%s' % msg.stamp)
        self.get_logger().info('名字:%s' % msg.host_name)
        self.get_logger().info('cpu:%s' % msg.cpu_percent)
        self.get_logger().info('内存：%s' % msg.memory_percent)
        self.get_logger().info('内存剩余：%s' % msg.memory_available)
        self.get_logger().info('网络发送%s' % msg.net_sent)
        self.get_logger().info('网络接受%s' % msg.net_recv)





def main():
    rclpy.init()
    node = StutsPub('stuts_pub')
    rclpy.spin(node)
    rclpy.shutdown()