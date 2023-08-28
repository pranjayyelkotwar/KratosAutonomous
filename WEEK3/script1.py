#!/usr/bin/env python3

import rospy
from beginner_tutorials.msg import Num
msg = Num()

if __name__ == '__main__':
    rospy.init_node('send_input')  #this node sends the input to user_input node
    pub = rospy.Publisher('user_input', Num, queue_size=10) #Input is the message name that is being sent to the topic 'user_input'

    while not rospy.is_shutdown():
        user_input = input("Enter w-s-a-d: ")  
        #input is used to accept input from the user. This is different from the above 'input' 
        if user_input.lower() in ['w', 's', 'a', 'd']:
            msg.direction = user_input.lower()
            pub.publish(msg)
