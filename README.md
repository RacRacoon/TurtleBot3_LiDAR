# TurtleBot3_LiDAR
# 🤖 TurtleBot3 ROS2 Humble Learning Journey

Dokumentasi langkah-langkah instalasi, simulasi, teleoperation, dan obstacle avoidance menggunakan TurtleBot3 pada ROS2 Humble.

---

# 1. Environment

## Sistem

- Ubuntu 22.04
- ROS2 Humble
- Gazebo
- TurtleBot3 Burger

---

# 2. Membuat Workspace

Buat workspace:

```bash
mkdir -p ~/turtlebot3_ws/src

cd ~/turtlebot3_ws/src
```

Clone package simulasi TurtleBot3:

```bash
git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
```

Kembali ke workspace:

```bash
cd ~/turtlebot3_ws
```

---

# 3. Install Dependency

Update package:

```bash
sudo apt update
```

Install package TurtleBot3:

```bash
sudo apt install ros-humble-turtlebot3
sudo apt install ros-humble-turtlebot3-msgs
```

Install dependency workspace:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

Jika muncul error 404:

```bash
sudo apt clean
sudo rm -rf /var/lib/apt/lists/*
sudo apt update
sudo apt upgrade -y
```

Kemudian ulangi:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

---

# 4. Build Workspace

```bash
cd ~/turtlebot3_ws

colcon build --symlink-install
```

Source workspace:

```bash
source install/setup.bash
```

Agar otomatis saat membuka terminal:

```bash
echo "source ~/turtlebot3_ws/install/setup.bash" >> ~/.bashrc
```

Reload:

```bash
source ~/.bashrc
```

---

# 5. Set Model TurtleBot3

Gunakan model Burger:

```bash
export TURTLEBOT3_MODEL=burger
```

Simpan permanen:

```bash
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc

source ~/.bashrc
```

Verifikasi:

```bash
echo $TURTLEBOT3_MODEL
```

Output:

```text
burger
```

---

# 6. Menjalankan Simulasi Gazebo

Buka terminal:

```bash
source /opt/ros/humble/setup.bash

source ~/turtlebot3_ws/install/setup.bash

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

World lain:

```bash
ros2 launch turtlebot3_gazebo empty_world.launch.py

ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
```

---

# 7. Mengecek Topic ROS2

Buka terminal baru:

```bash
ros2 topic list
```

Topic penting:

```text
/cmd_vel
/odom
/scan
/tf
/tf_static
```

---

# 8. Teleoperation Keyboard

Install package:

```bash
sudo apt install ros-humble-teleop-twist-keyboard
```

Jalankan:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Kontrol:

```text
u    i    o
j    k    l
m    ,    .
```

| Tombol | Aksi |
|---------|---------|
| i | Maju |
| , | Mundur |
| j | Belok kiri |
| l | Belok kanan |
| k | Stop |

---

# 9. Mengecek Data LiDAR

Lihat data mentah:

```bash
ros2 topic echo /scan
```

Data berasal dari:

```text
sensor_msgs/msg/LaserScan
```

Nilai `ranges` menunjukkan jarak obstacle dalam meter.

---

# 10. Visualisasi LiDAR di RViz

Jalankan:

```bash
rviz2
```

Tambahkan:

```text
LaserScan
```

Topic:

```text
/scan
```

LiDAR akan terlihat secara realtime.

---

# 11. Membuat Package Obstacle Avoidance

Masuk ke folder source:

```bash
cd ~/turtlebot3_ws/src
```

Buat package baru:

```bash
ros2 pkg create \
--build-type ament_python \
tb3_obstacle_avoid
```

Struktur:

```text
tb3_obstacle_avoid/
├── package.xml
├── setup.py
└── tb3_obstacle_avoid/
    └── avoid.py
```

---

# 12. Source Code Obstacle Avoidance

File:

```text
tb3_obstacle_avoid/tb3_obstacle_avoid/avoid.py
```

```python
import rclpy

from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class ObstacleAvoid(Node):

    def __init__(self):

        super().__init__('obstacle_avoid')

        self.sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

    def scan_callback(self, msg):

        cmd = Twist()

        front = min(
            list(msg.ranges[:20]) +
            list(msg.ranges[-20:])
        )

        if front < 0.5:

            cmd.linear.x = 0.0
            cmd.angular.z = 0.5

        else:

            cmd.linear.x = 0.15
            cmd.angular.z = 0.0

        self.pub.publish(cmd)


def main():

    rclpy.init()

    node = ObstacleAvoid()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

---

# 13. Konfigurasi setup.py

Tambahkan:

```python
entry_points={
    'console_scripts': [
        'avoid = tb3_obstacle_avoid.avoid:main',
    ],
},
```

---

# 14. Build Package

```bash
cd ~/turtlebot3_ws

colcon build --symlink-install
```

Source ulang:

```bash
source install/setup.bash
```

---

# 15. Menjalankan Obstacle Avoidance

Terminal 1:

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Terminal 2:

```bash
source ~/turtlebot3_ws/install/setup.bash

ros2 run tb3_obstacle_avoid avoid
```

Robot akan:

```text
Jalan maju
↓
Mendeteksi obstacle
↓
Berputar
↓
Menemukan jalur kosong
↓
Maju kembali
```

---

# 16. Arsitektur Sistem

```text
        LiDAR
       (/scan)
           │
           ▼
   Obstacle Avoid Node
           │
           ▼
       /cmd_vel
           │
           ▼
      TurtleBot3
```

---

# 17. Useful Commands

## List topic

```bash
ros2 topic list
```

## Echo topic

```bash
ros2 topic echo /scan
```

## List node

```bash
ros2 node list
```

## List package

```bash
ros2 pkg list | grep turtlebot3
```

## Rebuild workspace

```bash
cd ~/turtlebot3_ws

colcon build --symlink-install
```

## Source workspace

```bash
source ~/turtlebot3_ws/install/setup.bash
```

---

# 🚀 Next Step

Setelah tahap ini selesai, materi berikutnya:

1. SLAM Toolbox
2. Mapping Environment
3. Save Map
4. Localization
5. Navigation2
6. Autonomous Navigation
7. Camera Integration
8. YOLO Object Detection
9. Autonomous Inspection Robot

Roadmap:

```text
Teleop
  ↓
Obstacle Avoidance
  ↓
SLAM
  ↓
Navigation2
  ↓
Autonomous Robot
```