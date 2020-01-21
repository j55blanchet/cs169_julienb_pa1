#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Twist

MAX_SPEED = 0.2
rate_hz = 1

def main():
    rospy.init_node("moveforward")
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

    # Distance is specified as a parameter (in meters)
    distance = rospy.get_param("distance_m", default=1)
    distance_remaining = distance
    rate = rospy.Rate(rate_hz)

    rospy.loginfo("Rosbot will move forward {:d} meters".format(distance))
        
    while distance_remaining > 0:
    
        t = Twist()
        t.linear.x = min(distance_remaining, MAX_SPEED)
    
        rospy.loginfo("{0:d}m remaining. Moving forward at {1:d} m/s".format(distance_remaining, t.linear.x))
        distance_remaining -= t.linear.x
    
        pub.publish(t)
        rate.sleep()
    
    # Final message: tell the robot to stop
    pub.publish(Twist())
    rospy.loginfo("Finished moving forward.")


if __name__ == "__main__":
    main()
