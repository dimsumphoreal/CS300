#------------------------------------
# Name: Zachary Chin
# For: Lab03 for CS-300-A
# Date: February 26, 2020
#------------------------------------

# import modules
import time
import RPi.GPIO as GPIO

# set GPIO pin labelling to BCM
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins to input/output
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)       # set up switch as input (initial state is UP/HIGH/TRUE)
GPIO.setup(16, GPIO.OUT)                                  # set up LED as output

state = 1                                                 # Keeps track of the last state of the input 

#------------------------------------------------------------
# Callback function
# Input: BCM pin number
# Output: The channel that the edge was detected on && time
#------------------------------------------------------------
def my_callback(channel):
    print('Edge detected on BCM %s'%channel)
    print(time.time())

# Calls the callback function whenever the switch is released
# Releasing the switch causes a rising edge (LOW -> HIGH)
GPIO.add_event_detect(12, GPIO.RISING, callback = my_callback, bouncetime = 300)

# Set startTime equal to the current time
startTime = time.time()


# Runs the loop while the time elapsed (time.time() - startTime) without
#  any action (e.g. pressing the switch) is less than 5 seconds
# Once 5 seconds has passed without any action, the while loop ends
while (time.time() - startTime) < 5:
    
    # If the switch is pressed down and state == 1
    if GPIO.input(12) == False and state == 1:
        startTime = time.time()                         # Update startTime to the current time
        GPIO.output(16, True)                           # Turn on the LED
        time.sleep(0.5)
        state = 0

    # If the switch is pressed down and state == 0
    if GPIO.input(12) == False and state == 0:
        startTime = time.time()                         # Update startTime to the current time
        GPIO.output(16, False)                          # Turn off the LED
        time.sleep(0.5)
        state = 1

print("User inactive for too long, quitting program. Goodbye!")

# Clean up GPIO
GPIO.cleanup()