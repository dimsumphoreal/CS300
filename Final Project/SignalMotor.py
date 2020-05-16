#-------------------------------------------------------------------------
# SignalMotor.py
#
# Names: Brad Ritzema, Zachary Chin
# Course: CS-300-A
# Last Modified: 5/6/2020
#
# Publishes messages to the Raspberry Pi to control the locked/unlocked
#   state; linked with FrontDoorSecurity.py through MQTT.
#-------------------------------------------------------------------------
import paho.mqtt.client as mqtt
import time
import os

# Constants
BROKER = 'broker'       # insert broker name here
USERNAME = "cs300"      # broker username
PASSWORD = "safeIoT"    # broker password
PORT = 8883
QOS = 0
TOPIC = 'bdr22/door'
CERTS = '/etc/ssl/certs/ca-certificates.crt'
VALIDUNLOCK = "unlock1234"
VALIDLOCK = "lock1234"
LOCK_DELAY = 5

# Callback when a connection has been established with the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print('Connected to',BROKER)
    else:
        print('Connection to',BROKER,'failed. Return code=',rc)
        os._exit(1)

# While command incorrect: 
while True:
    command = input ("Enter unlock/lock command: ")
    if (command != VALIDLOCK and command != VALIDUNLOCK):
        print("Invalid unlock/lock command, try again")
    else:
        break

# Setup MQTT client and callbacks
client = mqtt.Client()
client.on_connect = on_connect

# Securely connect to MQTT broker
client.username_pw_set(username=USERNAME, password=PASSWORD)
client.tls_set(CERTS)
client.connect(BROKER, PORT, 60)
try:
    client.publish(TOPIC, command)
    print("Command successfully sent")
except KeyboardInterrupt:
    print("Done")
    client.disconnect()