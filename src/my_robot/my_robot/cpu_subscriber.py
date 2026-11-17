import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class CPUData(Node):
    def __init__(self):
        super().__init__('cpu_data')
        self.subscriber = self.create_subscription(String, '/cpu_monitor', self.cpu_callback,10)
        self.get_logger().info('CPU Data Subscriber Node has been started.')
    def cpu_callback(self, msg):
        self.get_logger().info(f"Received CPU Data: {msg.data}")    
def main(args=None):
    rclpy.init(args=args)
    node = CPUData()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()    