#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from psr_aula8_ex3_p3.msg import Dog


def callback(msg):
    rospy.loginfo("Received a dog named " + msg.name + ' which is ' + str(msg.age) +
                  ' years old')


def main():
    # ------------------------------------------------
    # Initialization
    # ------------------------------------------------
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("chatter", Dog, callback)

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    rospy.spin()

    # ------------------------------------------------
    # Termination
    # ------------------------------------------------


if __name__ == '__main__':
    main()
