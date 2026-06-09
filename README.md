# 🤖 TurtleBot3 LiDAR Learning Repository

A step-by-step ROS2 Humble learning repository for beginners who want to learn TurtleBot3 simulation, LiDAR processing, obstacle avoidance, SLAM, and autonomous navigation from scratch.

---

## 📖 About This Repository

This repository documents my learning journey with TurtleBot3 using ROS2 Humble and Gazebo.

Topics covered:

- TurtleBot3 Simulation
- ROS2 Fundamentals
- Topic & Node Communication
- LiDAR Data Processing
- Obstacle Avoidance
- RViz Visualization
- SLAM (Coming Soon)
- Navigation2 (Coming Soon)
- Autonomous Robotics (Coming Soon)

The goal is to provide a beginner-friendly roadmap from manual robot control to fully autonomous navigation.

---

## 🛠 Prerequisites

Before using this repository, make sure you have:

- Ubuntu 22.04
- ROS2 Humble
- Gazebo
- Python 3

Verify your ROS installation:

```bash
echo $ROS_DISTRO
```

Expected output:

```text
humble
```

---

## 🚀 Getting Started

### 1. Clone This Repository

```bash
git clone https://github.com/YOUR_USERNAME/TurtleBot3_LiDAR.git
```

Enter the workspace:

```bash
cd TurtleBot3_LiDAR
```

---

### 2. Clone TurtleBot3 Simulation Package

This repository does not include official TurtleBot3 simulation packages.

Clone them manually:

```bash
cd src

git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git

cd ..
```

---

### 3. Install Dependencies

```bash
sudo apt update

sudo apt install ros-humble-turtlebot3

sudo apt install ros-humble-turtlebot3-msgs

rosdep install --from-paths src --ignore-src -r -y
```

---

### 4. Build Workspace

```bash
colcon build --symlink-install
```

Source the workspace:

```bash
source install/setup.bash
```

---

### 5. Select TurtleBot3 Model

```bash
export TURTLEBOT3_MODEL=burger
```

Optional (make it permanent):

```bash
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc

source ~/.bashrc
```

---

### 6. Launch Gazebo Simulation

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

You should see:

- Gazebo Simulator
- TurtleBot3 Burger
- LiDAR Sensor
- Simulated Environment

---

### 7. Teleoperate the Robot

Install keyboard teleoperation:

```bash
sudo apt install ros-humble-teleop-twist-keyboard
```

Run:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Controls:

```text
u    i    o
j    k    l
m    ,    .
```

| Key | Action |
|------|---------|
| i | Move Forward |
| , | Move Backward |
| j | Turn Left |
| l | Turn Right |
| k | Stop |

---

### 8. Visualize LiDAR Data

Check available scan data:

```bash
ros2 topic echo /scan
```

Open RViz:

```bash
rviz2
```

Add:

```text
LaserScan
```

Topic:

```text
/scan
```

---

### 9. Run Obstacle Avoidance

Build the package:

```bash
colcon build --symlink-install

source install/setup.bash
```

Launch TurtleBot3:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Open a second terminal:

```bash
source install/setup.bash

ros2 run tb3_obstacle_avoid avoid
```

The robot will:

- Move forward
- Detect obstacles using LiDAR
- Rotate when obstacles are too close
- Continue moving when a path is clear

---

## 📂 Repository Structure

```text
TurtleBot3_LiDAR/
│
├── README.md
├── .gitignore
│
├── src/
│   └── tb3_obstacle_avoid/
│
└── docs/
    └── TUTORIAL.md
```

---

## 📚 Learning Roadmap

Current Progress:

```text
ROS2 Basics
    ✓

Gazebo Simulation
    ✓

Teleoperation
    ✓

LiDAR Processing
    ✓

Obstacle Avoidance
    ✓

SLAM Toolbox
    ⏳

Navigation2
    ⏳

Autonomous Navigation
    ⏳

Computer Vision
    ⏳
```

---

## 📘 Full Tutorial

For detailed step-by-step explanations, commands, and source code, see:

```text
docs/TUTORIAL.md
```

---

## 🎯 Future Improvements

- SLAM Toolbox integration
- Map saving and loading
- Localization
- Navigation2
- Camera integration
- YOLO object detection
- Autonomous inspection robot

---

## ⭐ Contributing

Feel free to fork this repository and experiment with your own TurtleBot3 projects.

If this repository helps you learn ROS2 and TurtleBot3, consider giving it a star.