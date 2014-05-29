#!/usr/bin/python

import os
import time
import sys
import pygame
from pygame.locals import *

pygame.init()

if pygame.joystick.get_count() == 0:
    print ("Error, I did not find any joysticks")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

while True:
    pygame.event.get()

    # Press back and start to quit this gamepad control application
    if joystick.get_button(8) == 1 and joystick.get_button(9) == 1:
        pygame.quit()
        sys.exit()

    # Press X + A + BACK to stop all ROS stuff on the robot
    if joystick.get_button(0) == 1 and joystick.get_button(1) == 1 and joystick.get_button(8) == 1:
        os.system("echo clearpath | sudo -S service husky-core stop")
        time.sleep(1) # Just to prevent keypress repeat

    # Press X + A + START to start all ROS stuff on the robot
    if joystick.get_button(0) == 1 and joystick.get_button(1) == 1 and joystick.get_button(9) == 1:
        os.system("echo clearpath | sudo -S service husky-core start")
        time.sleep(1) # Just to prevent keypress repeat

    # Press B + Y + START to start the scanning node
    if joystick.get_button(2) == 1 and joystick.get_button(3) == 1 and joystick.get_button(9) == 1:
        os.system("roslaunch ptu_laser_assembler husky_ptu_assembler.launch &")
        time.sleep(1) # Just to prevent keypress repeat
        
    # Press B + Y + STOP to stop the scanning node
    if joystick.get_button(2) == 1 and joystick.get_button(3) == 1 and joystick.get_button(8) == 1:
        os.system("pkill -SIGINT ptu_scan_assemb")
        time.sleep(1) # Just to prevent keypress repeat
