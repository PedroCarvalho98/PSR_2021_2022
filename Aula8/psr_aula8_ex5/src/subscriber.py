#!/usr/bin/python3
import argparse

import rospy
from std_msgs.msg import String
from psr_aula8_ex4.msg import Dog


def callbackMessageReceived(data):
    rospy.loginfo('Received a dog named ' + data.name + ' which is ' + str(data.age)
                  + ' years old')


def main():
    # ------------------------------------------------------
    # Initialization
    # ------------------------------------------------------
    parser = argparse.ArgumentParser(description='Ask topic')
    parser.add_argument('--topic', type = str, help='Topic1', default='chatter')
    args = vars(parser.parse_args())
    print(args)

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber(args['topic'], Dog, callbackMessageReceived)

    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------

    rospy.spin()


if __name__ == '__main__':
    main()