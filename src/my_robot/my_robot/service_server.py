import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool


class RobotService(Node):

    def __init__(self):
        super().__init__('robot_service')

        self.service = self.create_service(
            SetBool,
            'robot_power',
            self.power_callback
        )

        self.robot_on = False

    def power_callback(self, request, response):

        self.robot_on = request.data

        if self.robot_on:
            response.success = True
            response.message = 'Robot turned ON'
        else:
            response.success = True
            response.message = 'Robot turned OFF'

        return response


def main(args=None):

    rclpy.init(args=args)

    node = RobotService()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
