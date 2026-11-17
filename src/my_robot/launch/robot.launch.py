from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='my_robot',
            executable='publisher',
            name='publisher_node'
        ),

        Node(
            package='my_robot',
            executable='subscriber',
            name='subscriber_node'
        ),

        Node(
            package='my_robot',
            executable='service_server',
            name='robot_service'
        ),

        Node(
            package='my_robot',
            executable='action_server',
            name='robot_action_server'
        ),

        Node(
            package='my_robot',
            executable='parameter_node',
            name='robot_node',
            parameters=[
             'config/params.yaml'
                       ]
        )

    ])
