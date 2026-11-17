import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    package_path = get_package_share_directory('my_robot')
    urdf_path = os.path.join(
        package_path,
        'urdf',
        'drone.urdf'
    )
    with open(urdf_path, 'r') as file:
        drone_description = file.read()
    drone_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='drone_state_publisher',
        parameters=[
            {'robot_description': drone_description}
        ]
    )
    joint_state_publisher = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        parameters=[
            {'robot_description': drone_description}
        ]
    )
    return LaunchDescription([
        joint_state_publisher,
        drone_state_publisher
    ])