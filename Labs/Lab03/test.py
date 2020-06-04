import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)       # set up switch
GPIO.setup(16, GPIO.OUT)                                  # set up LED

state = 1           # Keeps track of the last state of the input (1: off; 0: on)

def my_callback(channel):
    print('Edge detected on BCM %s'%channel)
    print(time.time())

GPIO.add_event_detect(12, GPIO.RISING, callback = my_callback, bouncetime = 200)

while True:
    if GPIO.input(12) == True:
        print('HIGH')
    else:
        print('LOW')

GPIO.cleanup()
