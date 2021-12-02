#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from Aula9_ex.msg import Dog


def main():
    # ------------------------------------------------
    # Initialization
    # ------------------------------------------------
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chatter', Dog, queue_size=10)
    rate = rospy.Rate(10)

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    while not rospy.is_shutdown():
        dog = Dog()
        dog.name = 'boby'
        dog.age = 18
        dog.color = 'brown'
        dog.brothers.append('rosita')

        rospy.loginfo('Sending dog ...')  # same as print ... for now

        pub.publish(dog)  # finally, publish the message
        rate.sleep()

    # ------------------------------------------------
    # Termination
    # ------------------------------------------------


if __name__ == '__main__':
    main()
