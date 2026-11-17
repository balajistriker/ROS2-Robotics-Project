import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String 
class PressurePublisher(Node):
    def __init__(self):
        super().__init__('pressure_publisher')
        self.publisher = self.create_publisher(String,'/pre',10)
        self.timer= self.create_timer(10, self.publish_pressure)
        self.pressure =1013.25  # Initial pressure value in hPa
        self.get_logger().info('pressure publisher node has been started')
    def publish_pressure(self):
        msg = String()
        msg.data = f'pressure value received: {self.pressure}'
        self.publisher.publish(msg)
def main(args=None):
     rclpy.init()
     node =PressurePublisher()
     rclpy.spin(node)
     node.destroy_node()
     rclpy.shutdown()
if __name__=='__main__':
    main()                      