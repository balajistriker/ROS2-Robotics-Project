import rclpy 
from rclpy.node import Node
from std_msgs.msg import String 
class Temperaturepublisher(Node):

    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher = self.create_publisher(String, '/temperature',10)
        self.timer = self.create_timer(1.0, self.publish_temperature)
        self.temperature = 20.0  # Initial temperature value
        self.get_logger().info('Temperature publisher node has been started.')
    def publish_temperature(self):
             temperature = String()
             temperature.data = f"current temperature:{self.temperature}°C"
             self.publisher.publish(temperature)
def main(args=None):
       rclpy.init(args=args)
       node =Temperaturepublisher()
       rclpy.spin(node)
       node.destroy_node()
       rclpy.shutdown()
if __name__=='__main__':
        main()