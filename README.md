# ROS 2 Robotics Development

**Personal Robotics Engineering Project | Python | ROS 2 | Gazebo | URDF**

# 1. Project Overview

This repository contains my hands-on robotics development work using ROS 2 and Gazebo.

The objective is to develop a robotic platform with simulation, motion control, sensor integration, and autonomous navigation capabilities.

The project is being developed incrementally, starting with robot modelling and simulation and progressing toward autonomous mobile robotics.

## 2. Technology Stack

| Technology | Purpose |
|------------|---|
| Ubuntu Linux | Robotics development environment |
| ROS 2 | Robot middleware and communication |
| Python | Robotics node development |
| Gazebo | Robot simulation |
| URDF | Robot modelling |
| RViz2 | Robot visualization |
| TF2 | Coordinate frame management |
| LiDAR | Distance sensing and environment perception |
| IMU | Orientation and motion sensing |
| Git/GitHub | Version control |

## 3. Project Components

### Robot Modelling
- URDF-based robot description.
- Links and joints.
- Robot structure and geometry.
- Differential-drive robot modelling.

### Robot Simulation
- Gazebo simulation environment.
- Robot spawning.
- Robot movement and velocity control.
- ROS 2 and Gazebo communication.

### ROS 2 Communication
- Nodes.
- Publishers and subscribers.
- Topics and message communication.
- Services and actions (learning and implementation).

### Robot State and Motion
- Joint states.
- Odometry.
- TF and coordinate transformations.
- Differential-drive control.

### Sensor Integration
- LiDAR integration.
- IMU integration.
- Camera integration.

Sensor integration and validation are being developed incrementally.

## 4. Repository Structure

```text
ROS2-Robotics-Project/
│
├── README.md
│
└── src/
    └── my_robot/
        ├── urdf/
        │   ├── robot.urdf
        │   └── drone.urdf
        │
        ├── worlds/
        │   └── lidar_world.sdf
        │
        ├── launch/
        │
        ├── resource/
        │
        ├── test/
        │
        ├── package.xml
        ├── setup.py
        └── setup.cfg
```

*The structure above describes the main project files; additional files may be added as development progresses.*

## 5. Development Roadmap

| Feature | Status |
|---|---|
| ROS 2 workspace | Implemented |
| URDF robot modelling | Implemented |
| Links and joints | Implemented |
| Gazebo simulation | Implemented |
| Differential-drive control | Implemented |
| Velocity command integration | Implemented |
| Odometry | Implemented |
| TF integration | Implemented |
| ROS 2–Gazebo bridge | Implemented |
| LiDAR integration | Implemented |
| IMU integration | Implemented |
| Camera integration | Implemented |
| SLAM | Planned |
| Autonomous navigation using Nav2 | Planned |

*Status reflects the development progress of the project and should be updated as features are verified.*

## 6. Project Objective

My long-term objective is to develop intelligent autonomous mobile robots and apply robotics technologies to practical agricultural and industrial problems.

This project serves as the foundation for developing an autonomous agricultural rover.

## 7. Future Enhancements

- Complete multi-sensor integration.
- SLAM and environment mapping.
- Autonomous navigation.
- Obstacle detection and avoidance.
- Embedded hardware integration.
- Real-world robotic platform development.
**8> commands**
0.LIBGL_ALWAYS_SOFTWARE=1 QT_QPA_PLATFORM=xcb ign gazebo -r src/my_robot/worlds/lidar_world.sdf --- to start the gazebo
1.ros2 run robot_state_publisher robot_state_publisher src/my_robot/urdf/robot.urdf   ----for publishing the tf data on /tf and /tf_static 
2.ros2 run ros_gz_sim create -topic /robot_description -name my_robot --to spawned the robot in the gazebo
3.ros2 run ros_gz_bridge parameter_bridge '/world/empty/model/my_robot/joint_state@sensor_msgs/msg/JointState[ignition.msgs.Model' --ros-args -r /world/empty/model/my_robot/joint_state:=/joint_states 
(ros2 run ros_gz_bridge parameter_bridge '/world/lidar_world/model/my_robot/joint_state@sensor_msgs/msg/JointState[ignition.msgs.Model' --ros-args -r /world/lidar_world/model/my_robot/joint_state:=/joint_states)


4.ros2 run ros_gz_bridge parameter_bridge '/model/my_robot/cmd_vel@geometry_msgs/msg/Twist]ignition.msgs.Twist'
5.ros2 run ros_gz_bridge parameter_bridge   '/model/my_robot/odometrys@nav_msgs/msg/Odometry[ignition.msgs.Odometry' 
6.ign topic -e -t /model/my_robot/odometrys ^C
7.ros2 run my_robot odom_tf_broadcaster
8.ros2 run tf2_ros tf2_echo odom base_link
9. ros2 run ros_gz_bridge parameter_bridge \
  '/scan@sensor_msgs/msg/LaserScan[ignition.msgs.LaserScan'
[INFO] [1792928289.743263851] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/scan (ignition.msgs.LaserScan) -> /scan (sensor_msgs/msg/LaserScan)] (Lazy 0)

10.top
11.ros2 topic echo /joint_states
12.ros2 run ros_gz_bridge parameter_bridge   '/model/my_robot/odometrys@nav_msgs/msg/Odometry[ignition.msgs.Odometry' 
13.ign service -s /world/lidar_world/control   --reqtype ignition.msgs.WorldControl   --reptype ignition.msgs.Boolean   --timeout 1000   --req 'pause: false'  -----command to pause the gazebo simulation.
14.ros2 run ros_gz_bridge parameter_bridge '/imu@sensor_msgs/msg/Imu[ignition.msgs.IMU'    -----IMU bridge
15.ros2 topic pub --rate 10 /model/my_robot/cmd_vel geometry_msgs/msg/Twist "{linear: {x: -10.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
16.ign topic -l     ----- to check all gazebo topics 
17.Connect Depth Camera to ROS 2
Open another terminal:
ros2 run ros_gz_bridge parameter_bridge '/camera/depth/image_raw@sensor_msgs/msg/Image[ignition.msgs.Image'

18.ros2 run ros_gz_bridge parameter_bridge '/camera/camera_info@sensor_msgs/msg/CameraInfo[ignition.msgs.CameraInfo' -----Bridge the  CameraInfo topic
If Gazebo publishes /camera/camera_info for the depth camera, we can bridge it using:
19.Step 1: Bridge Depth CameraInfo to ROS 2
Run this in a new terminal: ros2 run ros_gz_bridge parameter_bridge '/camera/depth/camera_info@sensor_msgs/msg/CameraInfo[ignition.msgs.CameraInfo'

20, Step 3: Bridge the point cloud to ROS 2
If the message type is ignition.msgs.PointCloudPacked

  source /opt/ros/humble/setup.bash
source ~/robotics_ws/install/setup.bash

ros2 run ros_gz_bridge parameter_bridge '/camera/depth/image_raw/points@sensor_msgs/msg/PointCloud2[ignition.msgs.PointCloudPacked'

                                      ros2 topic list
                                     ros2 topic info /imu
                                    ros2 topic echo /imu --once

## 8. Developer
 Balaji 
B.Tech – Electronics and Communication Engineering

Interested in:
- Robotics Software Engineering.
- ROS 2 Development.
- Autonomous Mobile Robots.
- Embedded Robotics.
- Agricultural Robotics.

GitHub: https://github.com/balajistriker
