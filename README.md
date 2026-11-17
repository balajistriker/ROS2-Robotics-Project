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
# ============================================================
# ROS 2 HUMBLE + GAZEBO IGNITION COMMAND REFERENCE
# Workspace: ~/robotics_ws
# Robot Package: my_robot
# World: lidar_world
# ============================================================


# ============================================================
# 1. ENVIRONMENT SETUP
# ============================================================

source /opt/ros/humble/setup.bash
source ~/robotics_ws/install/setup.bash

echo $ROS_DISTRO


# ============================================================
# 2. START GAZEBO
# ============================================================

LIBGL_ALWAYS_SOFTWARE=1 QT_QPA_PLATFORM=xcb ign gazebo -r src/my_robot/worlds/lidar_world.sdf


# ============================================================
# 3. ROBOT STATE PUBLISHER
# Publishes robot transforms using URDF and joint states
# ============================================================

ros2 run robot_state_publisher robot_state_publisher src/my_robot/urdf/robot.urdf


# ============================================================
# 4. SPAWN ROBOT IN GAZEBO
# ============================================================

ros2 run ros_gz_sim create -topic /robot_description -name my_robot


# ============================================================
# 5. BRIDGE JOINT STATES: GAZEBO -> ROS 2
# ============================================================

ros2 run ros_gz_bridge parameter_bridge '/world/lidar_world/model/my_robot/joint_state@sensor_msgs/msg/JointState[ignition.msgs.Model' --ros-args -r /world/lidar_world/model/my_robot/joint_state:=/joint_states


# ============================================================
# 6. BRIDGE CMD_VEL: ROS 2 -> GAZEBO
# ============================================================

ros2 run ros_gz_bridge parameter_bridge '/model/my_robot/cmd_vel@geometry_msgs/msg/Twist]ignition.msgs.Twist'


# ============================================================
# 7. ROBOT MOVEMENT COMMANDS
# ============================================================

# Forward
ros2 topic pub --rate 10 /model/my_robot/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2}, angular: {z: 0.0}}"

# Backward
ros2 topic pub --rate 10 /model/my_robot/cmd_vel geometry_msgs/msg/Twist "{linear: {x: -0.2}, angular: {z: 0.0}}"

# Rotate
ros2 topic pub --rate 10 /model/my_robot/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0}, angular: {z: 0.2}}"

# Stop
ros2 topic pub --once /model/my_robot/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0}, angular: {z: 0.0}}"


# ============================================================
# 8. BRIDGE ODOMETRY: GAZEBO -> ROS 2
# ============================================================

ros2 run ros_gz_bridge parameter_bridge '/model/my_robot/odometrys@nav_msgs/msg/Odometry[ignition.msgs.Odometry'

# Inspect Gazebo odometry
ign topic -e -t /model/my_robot/odometrys


# ============================================================
# 9. CUSTOM ODOMETRY TF BROADCASTER
# ============================================================

ros2 run my_robot odom_tf_broadcaster

# Check odom -> base_link transformation
ros2 run tf2_ros tf2_echo odom base_link


# ============================================================
# 10. LIDAR BRIDGE
# GAZEBO -> ROS 2
# ============================================================

ros2 run ros_gz_bridge parameter_bridge '/scan@sensor_msgs/msg/LaserScan[ignition.msgs.LaserScan'

# Read LiDAR data
ros2 topic echo /scan


# ============================================================
# 11. IMU BRIDGE
# GAZEBO -> ROS 2
# ============================================================

ros2 run ros_gz_bridge parameter_bridge '/imu@sensor_msgs/msg/Imu[ignition.msgs.IMU'

# Inspect IMU information
ros2 topic info /imu

# Read one IMU message
ros2 topic echo /imu --once


# ============================================================
# 12. DEPTH CAMERA BRIDGE
# ============================================================

# Depth image
ros2 run ros_gz_bridge parameter_bridge '/camera/depth/image_raw@sensor_msgs/msg/Image[ignition.msgs.Image'

# Camera information
ros2 run ros_gz_bridge parameter_bridge '/camera/depth/camera_info@sensor_msgs/msg/CameraInfo[ignition.msgs.CameraInfo'

# Alternative camera information topic
ros2 run ros_gz_bridge parameter_bridge '/camera/camera_info@sensor_msgs/msg/CameraInfo[ignition.msgs.CameraInfo'

# Point cloud
ros2 run ros_gz_bridge parameter_bridge '/camera/depth/image_raw/points@sensor_msgs/msg/PointCloud2[ignition.msgs.PointCloudPacked'


# ============================================================
# 13. GAZEBO DEBUGGING
# ============================================================

# List Gazebo topics
ign topic -l

# Echo Gazebo odometry
ign topic -e -t /model/my_robot/odometrys


# ============================================================
# 14. ROS 2 TOPIC DEBUGGING
# ============================================================

# List topics
ros2 topic list

# Inspect topic
ros2 topic info /imu

# Read joint states
ros2 topic echo /joint_states

# Read LiDAR
ros2 topic echo /scan

# Read one IMU message
ros2 topic echo /imu --once

# List active nodes
ros2 node list


# ============================================================
# 15. ROS 2 SERVICES AND ACTIONS
# ============================================================

# List services
ros2 service list

# List actions
ros2 action list

# List installed packages
ros2 pkg list

# Find package location
ros2 pkg prefix my_robot

# List package executables
ros2 pkg executables my_robot


# ============================================================
# 16. PAUSE GAZEBO SIMULATION
# ============================================================

ign service -s /world/lidar_world/control \
--reqtype ignition.msgs.WorldControl \
--reptype ignition.msgs.Boolean \
--timeout 1000 \
--req 'pause: true'


# ============================================================
# 17. RESUME GAZEBO SIMULATION
# ============================================================

ign service -s /world/lidar_world/control \
--reqtype ignition.msgs.WorldControl \
--reptype ignition.msgs.Boolean \
--timeout 1000 \
--req 'pause: false'


# ============================================================
# 18. SYSTEM PERFORMANCE MONITORING
# ============================================================

top


# ============================================================
# 19. BUILD ROS 2 WORKSPACE
# ============================================================

cd ~/robotics_ws
colcon build --symlink-install

source install/setup.bash


# ============================================================
# 20. ROS 2 ENVIRONMENT CHECK
# ============================================================

echo $ROS_DISTRO

printenv | grep ROS


# ============================================================
# END OF COMMAND REFERENCE
# ============================================================

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
