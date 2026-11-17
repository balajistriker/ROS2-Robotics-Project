import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from example_interfaces.action import Fibonacci


class RobotActionServer(Node):

    def __init__(self):
        super().__init__('robot_action_server')

        self.action_server = ActionServer(
            self,
            Fibonacci,
            'robot_task',
            self.execute_callback
        )

    def execute_callback(self, goal_handle):

        self.get_logger().info('Goal received')

        feedback_msg = Fibonacci.Feedback()

        feedback_msg.sequence = [0, 1]

        for i in range(1, goal_handle.request.order):

            if goal_handle.is_cancel_requested:
                goal_handle.canceled()

                self.get_logger().info('Goal cancelled')

                return Fibonacci.Result()

            feedback_msg.sequence.append(
                feedback_msg.sequence[-1]
                + feedback_msg.sequence[-2]
            )

            goal_handle.publish_feedback(feedback_msg)

            self.get_logger().info(
                f'Progress: {feedback_msg.sequence}'
            )

            time.sleep(1)

        goal_handle.succeed()

        result = Fibonacci.Result()

        result.sequence = feedback_msg.sequence

        return result


def main(args=None):

    rclpy.init(args=args)

    node = RobotActionServer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
