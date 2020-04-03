###########################################################
# Author: Derek Schuurman
# Edited by: Zach Chin
# Date: 04/01/2020
# Assignment: CS 300 Lab 07
# Class: LED-mqtt.py
# 
# Description: 
#   Waits for a message from mqtt-button.py to turn two
#   LEDs on and off. Each button on mqtt-button.py controls
#   one of the two LEDs from this class. Connects to an
#   MQTT broker to receive the messages.
###########################################################

import RPi.GPIO as GPIO  
import paho.mqtt.client as mqtt
import time

# Constants 
BROKER = 'test.mosquitto.org' 
PORT = 1883 
QOS = 0 
LED1 = 16 
LED2 = 12
MESSAGE1 = 'Button for red LED pressed'
MESSAGE2 = 'Button for yellow LED pressed'

# Setup GPIO mode 
GPIO.setmode(GPIO.BCM)

# Configure GPIO for LED output 
GPIO.setup(LED1, GPIO.OUT) 
GPIO.setup(LED2, GPIO.OUT) 

# Callback when a connection has been established with the MQTT broker 
def on_connect(client, userdata, rc, *extra_params):   
    print('Connected with result code='+str(rc))

# Callback when client receives a message from the broker 
# Use button message to turn LED on/off 
def on_message(client, data, msg):  
    # Decodes the message received from the broker to a string
    str_message = str(msg.payload.decode("utf-8"))
    
    # If statements to determine which message has been received in order
    #   to activate the correct LED
    if msg.topic == "zc26/button" and  str_message == MESSAGE1:             
        if GPIO.input(LED1) == 1:          
            GPIO.output(LED1, 0)       
        else:          
            GPIO.output(LED1, 1)
    elif msg.topic == "zc26/button" and  str_message == MESSAGE2:             
        if GPIO.input(LED2) == 1:          
            GPIO.output(LED2, 0)       
        else:          
            GPIO.output(LED2, 1)


# Setup MQTT client and callbacks 
client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message

# Connect to MQTT broker and subscribe to the button topic 
client.connect(BROKER, PORT, 60) 
client.subscribe("zc26/button", qos=QOS) 
client.loop_start()

client.loop_start() 
while True:   
    time.sleep(10)

print("Done") 
client.disconnect() 
GPIO.cleanup()       # clean up GPIO
