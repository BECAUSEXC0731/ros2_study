
import espeakng    #遇到问题导入失败，原因是Pylance 有时缓存旧状态Restart Language Server就可以了
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
import queue
import threading
import time


class Subscriber(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.sub_queue= queue.Queue()
        self.get_logger().info("正在创建订阅者...")
        self.subscriber_=self.create_subscription(String,"topic_learn",self.subscriber_callback,10)
        self.speak_thread=threading.Thread(target=self.speak)
        self.speak_thread.start()


    def subscriber_callback(self,msg):
        self.sub_queue.put(msg.data)
        self.get_logger().info(f"收到数据: {msg.data}")

    def speak(self):
        speaker = espeakng.Speaker()
        speaker.voice = 'en'


        while rclpy.ok():
            if not self.sub_queue.empty():
                text = self.sub_queue.get()
                speaker.say(text)
                speaker.wait()
            else:
                time.sleep(1)



def main():
    rclpy.init()
    node=Subscriber("subscriber")
    node.get_logger().info("订阅者已经启动！")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()