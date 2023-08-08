#! /usr/bin/env python3
 
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
 
disToObstacle = 0.55
 
def callback(msg):
	print(f"Distance is {msg.ranges[0]}")
	if msg.ranges[0] <= disToObstacle :
		move.angular.z = 1
		move.linear.x = 0
		pub.publish(move)
		#speed changed
		rospy.sleep(0.4)
	move.linear.x = 0.5
	move.angular.z = 0
	pub.publish(move)

rospy.init_node('Week2')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(2)
move = Twist()

rospy.spin()
