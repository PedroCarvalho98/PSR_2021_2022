#!/usr/bin/python3
import argparse

import rospy
from std_msgs.msg import String


def callbackMessageReceived(data):
    rospy.loginfo(rospy.get_caller_id() + "%s", data.data)


def main():
    # ------------------------------------------------------
    # Initialization
    # ------------------------------------------------------
    parser = argparse.ArgumentParser(description='Ask topic')
    parser.add_argument('--topic', type = str, help='Topic1', default='chatter')
    args = vars(parser.parse_args())
    print(args)

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber(args['topic'], String, callbackMessageReceived)

    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------

    rospy.spin()


if __name__ == '__main__':
    main()