#!/usr/bin/env python
""" odom_subscriber.py

    A simple node that republishes pose messages. Not useful practically,
    but it gives us practice with creating subscribers and publishers
"""
import rospy
from std_msgs.msg import Header
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

def main():
    rospy.init_node("odom_subscriber")
    plot_pub = rospy.Publisher("/plot_xy", PoseStamped, queue_size=1)

    def odom_msg_received(msg):
        out_msg = PoseStamped()
        out_msg.header = Header()
        out_msg.header.frame_id = msg.header.frame_id
        out_msg.pose = msg.pose
        plot_pub.publish(out_msg)

    rospy.Subscriber("/pose", PoseStamped, odom_msg_received)
    rospy.spin()

if __name__ == "__main__":
    main()