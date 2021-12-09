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
    parser.add_argument('--topic1', type = str, help='Topic1', default='A1')
    parser.add_argument('--topic2', type=str, help='Topic2')
    args = vars(parser.parse_args())
    print(args)

    rospy.init_node('Sub', anonymous=True)

    rospy.Subscriber(args['topic1'], String, callbackMessageReceived)
    if not args['topic2'] is None:
        rospy.Subscriber(args['topic2'], String, callbackMessageReceived)

    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------

    rospy.spin()


if __name__ == '__main__':
    main()