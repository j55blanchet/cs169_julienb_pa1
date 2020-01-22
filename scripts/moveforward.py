#!/usr/bin/env python
"""
    moveforward.py

    Author: Julien Blanchet
    Jan. 20 2020

    A simple ROS node that will publish velocity commands instructing 
    the robot to move forward in a straight line a specified distance.
"""

import rospy
from geometry_msgs.msg import Twist

MAX_SPEED = 0.2 # Max speed to instruct the robot to go, in m/s
RATE_HZ = 1     # Rate at which to publish velocity commands (and to print to console)

def main():
    rospy.init_node("moveforward")
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

    # Distance is specified as a parameter (in meters)
    distance = rospy.get_param("distance_m", default=1.0)
    distance_remaining = distance
    rate = rospy.Rate(RATE_HZ)

    rospy.loginfo("Rosbot will move forward {:f} meters".format(distance))
    rospy.loginfo("Sleeping for 5 seconds to allow for serial bridge to get operational")
    rospy.sleep(rospy.Duration(secs=5))

    while distance_remaining > 0:
    
        t = Twist()
        t.linear.x = min(distance_remaining, MAX_SPEED)
    
        rospy.loginfo("{0:f}m remaining. Moving forward at {1:f} m/s".format(distance_remaining, t.linear.x))
        distance_remaining -= t.linear.x / rate_hz
    
        pub.publish(t)
        rate.sleep()
    
    # Final message: tell the robot to stop
    pub.publish(Twist())
    rospy.loginfo("Finished moving forward.")

if __name__ == "__main__":
    main()
