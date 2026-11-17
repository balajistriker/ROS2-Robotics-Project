import rclpy
from rclpy.node import Node


class RobotNode(Node):

    def __init__(self):
        super().__init__('robot_node')

        self.declare_parameter('robot_name', 'my_robot')
        self.declare_parameter('max_speed', 1.0)

        robot_name = self.get_parameter(
            'robot_name'
        ).value

        max_speed = self.get_parameter(
            'max_speed'
        ).value

        self.get_logger().info(
            f'Robot: {robot_name}'
        )

        self.get_logger().info(
            f'Max speed: {max_speed}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = RobotNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
