# !/bin/bash

set -e
set -v

source /opt/ros/fuerte/setup.bash
export ROS_PACKAGE_PATH="/home/administrator/ros_uLaval":$ROS_PACKAGE_PATH

screen -d -m python /home/administrator/GamepadControl/GamepadDaemon.py
