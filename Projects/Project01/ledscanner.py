#------------------------------------
# Name: Zachary Chin and Juli Lim
# 
# For: Project 01 for CS-300-A
# Date: March 11, 2020
#------------------------------------

# import modules
import time
import RPi.GPIO as GPIO

# set GPIO pin labelling to BCM
GPIO.setmode(GPIO.BCM)

# define states
state = 0
STATE1 = 1			# first state
STATE2 = 2			# second state
STATE3 = 3			# third state
STATE4 = 4			# fourth state
STATE5 = 5			# fifth state
STATE6 = 6			# sixth state

# define GPIO port numbers
LED1 = 23
LED2 = 24
LED3 = 25
LED4 = 16
LED5 = 20
LED6 = 21

# set up GPIO pins
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(LED5, GPIO.OUT)
GPIO.setup(LED6, GPIO.OUT)

FORWARD = 0		# initial direction (forward)
BACKWARD = 1

state = STATE1
direction = FORWARD

while True:
	# if GPIO.input(switch) == True:
    if state == STATE1 and direction == FORWARD:
        print("LED1 on\n")
        GPIO.output(LED1, True)
        time.sleep(0.2)
        state = 2
    elif state == STATE2 and direction == FORWARD:
        print("LED1 off")
        print("LED2 on\n")
        GPIO.output(LED1, False)
        GPIO.output(LED2, True)
        time.sleep(0.2)
        state = 3
    elif state == STATE3 and direction == FORWARD:
        print("LED2 off")
        print("LED3 on\n")
        GPIO.output(LED2, False)
        GPIO.output(LED3, True)
        time.sleep(0.2)
        state = 4
    elif state == STATE4 and direction == FORWARD:
        print("LED3 off")
        print("LED4 on\n")
        GPIO.output(LED3, False)
        GPIO.output(LED4, True)
        time.sleep(0.2)
        state = 5
    elif state == STATE5 and direction == FORWARD:
        print("LED4 off")
        print("LED5 on\n")
        GPIO.output(LED4, False)
        GPIO.output(LED5, True)
        time.sleep(0.2)
        state = 6
    elif state == STATE6 and direction == FORWARD:
        print("LED5 off")
        print("LED6 on\n")
        GPIO.output(LED5, False)
        GPIO.output(LED6, True)
        time.sleep(0.2)
        direction = BACKWARD

    # BACKWARD
    elif state == STATE6 and direction == BACKWARD:
        # print("LED6 off\n")
        GPIO.output(LED6, False)
        GPIO.output(LED5, True)
        time.sleep(0.2)
        state = 5
    elif state == STATE5 and direction == BACKWARD:
        # print("LED1 off")
        # print("LED2 on\n")
        GPIO.output(LED5, False)
        GPIO.output(LED4, True)
        time.sleep(0.2)
        state = 4
    elif state == STATE4 and direction == BACKWARD:
        # print("LED2 off")
        # print("LED3 on\n")
        GPIO.output(LED4, False)
        GPIO.output(LED3, True)
        time.sleep(0.2)
        state = 3
    elif state == STATE3 and direction == BACKWARD:
        # print("LED3 off")
        # print("LED4 on\n")
        GPIO.output(LED3, False)
        GPIO.output(LED2, True)
        time.sleep(0.2)
        state = 2
    elif state == STATE2 and direction == BACKWARD:
        # print("LED4 off")
        # print("LED5 on\n")
        GPIO.output(LED2, False)
        GPIO.output(LED1, True)
        time.sleep(0.2)
        state = 1

    elif state == STATE1 and direction == BACKWARD:
        # print("LED5 on")
        # print("LED6 off\n")
        direction = FORWARD

	# Scanner in reverse direction
	# if GPIO.input(switch) == False:
		#forward = False
		# if state == 1 and forward == False:
		# 	print("LED1 on\n")
		# 	#If LED6 is on:							# if GPIO.input(12) == True:
		# 	#print("LED6 off\n")
		# 	time.sleep(1)
		# 	state = 2
		# elif state == 2 and forward == False:
		# 	print("LED1 off")
		# 	print("LED2 on\n")
		# 	time.sleep(1)
		# 	state = 3
		# elif state == 3 and forward == False:
		# 	print("LED off")
		# 	print("LED3 on\n")
		# 	time.sleep(1)
		# 	state = 4
		# elif state == 4 and forward == False:
		# 	print("LED3 off")
		# 	print("LED4 on\n")
		# 	time.sleep(1)
		# 	state = 5
		# elif state == 5 and forward == False:
		# 	print("LED5 off")
		# 	print("LED5 on\n")
		# 	time.sleep(1)
		# 	state = 6
		# elif state == 6 and forward == False:
		# 	print("LED1 off")
		# 	print("LED6 on\n")
		# 	time.sleep(1)
		# 	state = 1
