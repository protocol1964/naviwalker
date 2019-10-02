#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import tf


def main():
    rospy.init_node("naviwalker_test")
    rate = rospy.Rate(60)

    while not rospy.is_shutdown():
        rate.sleep()

    rospy.spin()


if __name__ == "__main__":
    main()
