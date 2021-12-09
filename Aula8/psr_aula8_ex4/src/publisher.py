#!/usr/bin/python3
import argparse

import rospy
from std_msgs.msg import String
from psr_aula8_ex4.msg import Dog


def main():
    # ------------------------------------------------------
    # Initialization
    # ------------------------------------------------------
    parser = argparse.ArgumentParser(description='Ask rate and topic')
    parser.add_argument('--rate', type = float, help='Rate of printed messages', default=1)
    # parser.add_argument('--topic', type = str, help='Topic', default='A1')
    parser.add_argument('--message', type = str, help = 'Message to send', default = 'I do not know what to say')
    args = vars(parser.parse_args())
    print(args)

    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    pub2 = rospy.Publisher('A17', String, queue_size=10)
    rate = rospy.Rate(args['rate'])  # 1hz

    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------

    while not rospy.is_shutdown():
        message_to_send = args['message'] + ' ' + str(rospy.get_time())
        rospy.loginfo(message_to_send)
        pub.publish(message_to_send)
        pub2.publish('Aqui vai um para sul')
        rate.sleep()


if __name__ == '__main__':
    main()
