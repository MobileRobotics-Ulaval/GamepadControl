#!/usr/bin/python

import os
import time
import sys
import pygame
from pygame.locals import *
from tendo import singleton

# This line prevent multiple executions of this script at the same time
me = singleton.SingleInstance()

userPassword = "clearpath" # to run "sudo" commands
sleepTimeAfterExecCmd = 1 # in second

defaultJoystickID = 0

buttonX = 0
buttonA = 1
buttonB = 2
buttonY = 3
buttonLB = 4
buttonRB = 5
buttonLT = 6
buttonRT = 7
buttonBACK = 8
buttonSTART = 9
buttonLeftAxis = 10
buttonRightAxis = 11
# I restricted myself to the 0/1 buttons ...

pygame.init()

if pygame.joystick.get_count() == 0:
    print ("Error, I did not find any joysticks")
else:
    joystick = pygame.joystick.Joystick(defaultJoystickID)
    joystick.init()

while True:
    pygame.event.wait() # Prevent from using all resources
    pygame.event.get()

    if joystick.get_button(buttonX) and joystick.get_button(buttonA) and joystick.get_button(buttonY) and joystick.get_button(buttonB) and joystick.get_button(buttonLT) and joystick.get_button(buttonLB) and joystick.get_button(buttonBACK):
        os.system("echo " + userPassword + " | sudo -S shutdown now")
        time.sleep(sleepTimeAfterExecCmd) # Just to prevent keypress repeat
            
    elif joystick.get_button(buttonBACK) and joystick.get_button(buttonSTART):
        pygame.quit()
        sys.exit()

    elif joystick.get_button(buttonX) and joystick.get_button(buttonA) and joystick.get_button(buttonBACK):
        os.system("echo " + userPassword + " | sudo -S service husky-core stop")
        time.sleep(sleepTimeAfterExecCmd) # Just to prevent keypress repeat

    elif joystick.get_button(buttonX) and joystick.get_button(buttonA) and joystick.get_button(buttonSTART):
        os.system("echo " + userPassword + " | sudo -S service husky-core start")
        time.sleep(sleepTimeAfterExecCmd) # Just to prevent keypress repeat

    elif joystick.get_button(buttonB) and joystick.get_button(buttonY) and joystick.get_button(buttonSTART):
        os.system("roslaunch /home/administrator/ros_uLaval/ptu_laser_assembler/launch/husky_ptu_assembler.launch &")
        time.sleep(sleepTimeAfterExecCmd) # Just to prevent keypress repeat
        
    elif joystick.get_button(buttonB) and joystick.get_button(buttonY) and joystick.get_button(buttonBACK):
        os.system("pkill -SIGINT ptu_scan_assemb")
        time.sleep(sleepTimeAfterExecCmd) # Just to prevent keypress repeat
        
        
        
        
