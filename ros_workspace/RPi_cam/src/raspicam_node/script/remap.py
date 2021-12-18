#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image, CameraInfo



def image_cb(data):
    image_pub.publish(data)

def info_cb(data):
    info_pub.publish(data)




if __name__ == '__main__':
    rospy.init_node('remapping_node')
    image_pub = rospy.Publisher("/camera_image", Image, queue_size=10)
    info_pub = rospy.Publisher("/camera_info", CameraInfo, queue_size=10)
    rospy.Subscriber("raspicam_node/image_raw", Image, image_cb)
    rospy.Subscriber("raspicam_node/camera_info", CameraInfo, info_cb)
    while not rospy.is_shutdown():
	rospy.spin()
