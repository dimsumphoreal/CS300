#------------------------------------
# Name: Zachary Chin
# For: Lab03 for CS-300-A
# Date: February 26, 2020
#------------------------------------

# import modules
import time
#import RPi.GPIO as GPIO

## set GPIO pin labelling to BCM
#GPIO.setmode(GPIO.BCM)

state = 1			# first state
direction = 0		# direction

while True:
	# if GPIO.input(switch) == True:
	if state == 1 and direction == 0:
		print("LED1 on\n")
		#If LED6 is on:							# if GPIO.input(12) == True:
			#print("LED6 off\n")
		time.sleep(1)
		state = 2
	elif state == 2 and direction == 0:
		print("LED1 off")
		print("LED2 on\n")
		time.sleep(1)
		state = 3
	elif state == 3 and direction == 0:
		print("LED2 off")
		print("LED3 on\n")
		time.sleep(1)
		state = 4
	elif state == 4 and direction == 0:
		print("LED3 off")
		print("LED4 on\n")
		time.sleep(1)
		state = 5
	elif state == 5 and direction == 0:
		print("LED4 off")
		print("LED5 on\n")
		time.sleep(1)
		state = 6
	elif state == 6 and direction == 0:
		print("LED5 off")
		print("LED6 on\n")
		time.sleep(1)
		direction = 1

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