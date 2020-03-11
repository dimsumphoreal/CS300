###########################################################
# Student name: Juli Lim and Zach Chin
# Date: 03/10/2020
# Assignment: CS 300 Lab05
# Class: Servomotor.py
# 
# Description: 
#   Waits for a switch to be pressed; once the switch is 
#   pressed, the servomotor moves to a random position in
#   its range from -90 to 90 degrees.
###########################################################

import time
import pigpio
import random


# Constants
MOTOR = 18              # Connect servomotor to BCM 18
SWITCH = 12             # Connect switch to BCM 12
WAIT_FOR_BUTTON = 0     # Set WAIT_FOR_BUTTON state to 0
RANDOM_MOVE = 1         # Set RANDOM_MOVE state to 1

pi = pigpio.pi()
if not pi.connected:
    exit(0)

# set servomotor to default state
pi.set_servo_pulsewidth(MOTOR, 0)

# set switch to default state
pi.set_pull_up_down(SWITCH, pigpio.PUD_DOWN)

# set glitch filter for switch at 200 microseconds
pi.set_glitch_filter(SWITCH, 200)

# default state variable
state = WAIT_FOR_BUTTON

#########################################################
# Function: move_to_angle
#   Calculates and sets the pulsewidth of the servomotor
#   based on a random degree
# 
#########################################################
def move_to_angle():
        randomdeg = random.randint(-90,90)
        pulsewidth = (100/18) * randomdeg + 1500
        pi.set_servo_pulsewidth(MOTOR, pulsewidth)
        print("Degree: " + str(randomdeg) + "; "
            + "Pulsewidth: " + str(pulsewidth))


#########################################################
# Function: user_callback
#   Changes the current state to RANDOM_MOVE
#
# Input: gpio, level, tick
#
#########################################################

def user_callback(gpio, level, tick):
    global state
    state = RANDOM_MOVE

# variable for callback (detects a rising edge on the switch)
cb1 = pi.callback(SWITCH, pigpio.RISING_EDGE, user_callback)

try: 
    # entering into a forever loop
    while True:    
        if (state == RANDOM_MOVE):
            move_to_angle()
            # change state back to WAIT_FOR_BUTTON
            state = WAIT_FOR_BUTTON
            
except KeyboardInterrupt:
    cb1.cancel() # cancel callback cb1
