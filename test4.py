#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from rospy.exceptions import ROSInterruptException
import time

def move_in_circle(velocity_publisher):
  velocity_message = Twist()
  velocity_message.linear.x = 1
  velocity_message.angular.z = 1
  loop_rate=rospy.Rate(10)
  t0=rospy.Time.now().to_sec()
  ini_dis = 3.14
  while True:
    rospy.loginfo("My turtlebot is: Moving in a circle!")
    velocity_publisher.publish(velocity_message)
    t1 = rospy.Time.now().to_sec()
    curr_dis = (t1-t0)*1
    if (curr_dis >= ini_dis):
      velocity_message.linear.x=0
      velocity_message.angular.z=0
      velocity_publisher.publish(velocity_message)
      break

def rotate(velocity_publisher):
  velocity_message = Twist()
  angular_speed_radian = math.radians(20)
  velocity_message.angular.z = angular_speed_radian
  loop_rate = rospy.Rate(10)
  t0=rospy.Time.now().to_sec()
  angle = 90
  while True:
    rospy.loginfo("My turtlebot is: Rotating!")
    velocity_publisher.publish(velocity_message)
    t1=rospy.Time.now().to_sec()
    curr_angle = (t1-t0)*20
    if (curr_angle >= angle):
      velocity_message.angular.z = 0
      velocity_publisher.publish(velocity_message)
      break

def move_in_dia(velocity_publisher):
  velocity_message = Twist()
  velocity_message.linear.x = 2
  loop_rate = rospy.Rate(10)
  t0=rospy.Time.now().to_sec()
  while True:
    rospy.loginfo("My turtlebot is: Moving straight!")
    velocity_publisher.publish(velocity_message)
    t1=rospy.Time.now().to_sec()
    dis = (t1-t0)*2
    if (dis >= 2):
      break
  velocity_message.linear.x = 0
  velocity_publisher.publish(velocity_message)

rospy.init_node("task_0",anonymous=True)
velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
time.sleep(2)
move_in_circle(velocity_publisher)
rotate(velocity_publisher)
move_in_dia(velocity_publisher)
