#学习知识：发布者的创建
#功能：创建一个发布者节点，定时发布消息到指定话题


import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from queue import Queue
 


class Publisher(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info("node has been created")
        self.publisher_queue=Queue()
        self.publisher_ = self.create_publisher(String,"topic_learn",10)
        self.create_timer(1,self.timer_callback)

    def timer_callback(self):
        self.publisher_queue.put("hello world")
        if self.publisher_queue.qsize()>0:
            msg=String()
            msg.data=self.publisher_queue.get()
            self.publisher_.publish(msg)
            self.get_logger().info(f"publish message: {msg.data}")
            


def main():
    rclpy.init()
    node=Publisher("publisher")
    node.get_logger().info("发布者已经启动！")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()