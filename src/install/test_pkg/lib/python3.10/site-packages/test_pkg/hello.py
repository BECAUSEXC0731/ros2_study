import rclpy 
from rclpy.node import Node  

def main():
    rclpy.init()
    node = Node("name")
    node.get_logger().info('你好世界') 
    node.get_logger().warn('你好世界') 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()