from setuptools import find_packages, setup

import os 
from glob import glob
package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #Launch_Files
        (
          os.path.join('share',package_name,'launch'),
          glob('launch/*.py')
        ),
        #YAML configuration files
        (
         os.path.join('share',package_name,'config'),
         glob('config/*.yaml')
         ),
        #URDF files
        (
        os.path.join('share',package_name,'urdf'),
        glob('urdf/*')
        ),
        (
        os.path.join('share', package_name, 'meshes'), glob('meshes/*')
        )
         
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='balaji',
    maintainer_email='balaji@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'publisher = my_robot.publisher:main',
        'subscriber =my_robot.subscriber:main',
        'service_server =my_robot.service_server:main',
        'action_server =my_robot.action_server:main',
        'parameter_node = my_robot.parameter_node:main',
        'odom_tf_broadcaster = my_robot.odom_tf_broadcaster:main',
        'temperature_publisher = my_robot.temperature_publisher:main',
        'pressure_publisher = my_robot.pressure_publisher:main',
        'cpu_monitor_publisher = my_robot.cpu_monitor_publisher:main',
        'cpu_subscriber = my_robot.cpu_subscriber:main'
        ],
    },
)
