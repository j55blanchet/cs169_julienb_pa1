import rospy
from geometry_msgs.msg import PoseStamped
from visualization_msgs.msg import Marker

def main():
    rospy.init_node("odom_subscriber")

    def odom_msg_received(msg):
        rospy.logdebug("Odom message received", msg)

    rospy.Subscriber("/odom", PoseStamped, odom_msg_received)
    rospy.spin()
    

if __name__ == "__main__":
    main()