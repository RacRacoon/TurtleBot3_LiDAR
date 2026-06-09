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
