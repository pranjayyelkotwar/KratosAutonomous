#!/usr/bin/env python3

import rospy
from beginner_tutorials.msg import Num
from geometry_msgs.msg import Twist



def callback(msg):
   command = msg.direction
   twist = Twist()
   if command == 'w':
      twist.linear.x = 0.5
   elif command == 's':
      twist.linear.x = -0.5
   elif command == 'a':
      twist.angular.z = 0.785
   elif command == 'd':
      twist.angular.z = -0.785
   pub.publish(twist)
   rospy.sleep(2)
   twist.linear.x = 0
   twist.angular.z = 0
   pub.publish(twist)
   
if __name__ == '__main__':
   rospy.init_node('executioner')  
   rospy.Subscriber('user_input', Num, callback) 
   pub = rospy.Publisher('/cmd_vel', Twist ,queue_size=10)
   rospy.spin()
