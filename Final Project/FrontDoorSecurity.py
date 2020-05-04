# doorLock.py
# Note: enter "sudo pigpiod" prior to starting the program
import RPi.GPIO as GPIO
import time
import pigpio
import paho.mqtt.client as mqtt
import os

# For camera and Gmail
from datetime import datetime
from picamera import PiCamera
import html
import mimetypes
from email.headerregistry import Address
from email.message import EmailMessage
from email.utils import make_msgid
from pathlib import Path
import smtplib
import ssl

# Create camera object
camera = PiCamera()

# Constants for doorbell
DOORBELL = 12

# Constants for porch light
MOTION_SENSOR = 23
LED = 16

# Constants for servo motor
MOTOR = 18              #Connect servomotor to BCM 18
DELAY = 2               #Delay to avoid bouncing
LOCKPOSITION = 1500
UNLOCKPOSITION = 2300
TIMEBUFFER = 10

# Constants for mqtt
BROKER = 'iot.cs.calvin.edu'
USERNAME = "cs300" # broker username
PASSWORD = "safeIoT" # broker password
PORT = 8883
QOS = 0
TOPIC = 'bdr22/door'
CERTS = '/etc/ssl/certs/ca-certificates.crt'
VALIDUNLOCK = "b'unlock1234'"
VALIDLOCK = "b'lock1234'"

# Constants for Gmail
GMAIL_SERVER = 'smtp.gmail.com'
GMAIL_PORT = 465
GMAIL_USER = "zcdev6@gmail.com"
GMAIL_PASS = "Isathwbbofb1sjfomasddr2"

# Mailing list
sent_to = ["zcdev6@gmail.com"]


# setup doorbell
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOORBELL, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# setup porch light and sensor
GPIO.setup(MOTION_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)


# Function to email picture
def send_email(dateAndTime, imgName):
    title = dateAndTime.strftime("%Y%m%d-%H%M")
    path = Path(imgName)

    msg = EmailMessage()
    msg["Subject"] = "Front Door [" + dateAndTime.strftime("%Y-%m-%d @ %H:%M:%S") + "]"
    msg["From"] = GMAIL_USER
    msg["To"] = sent_to

    # Specify content of email shown in inbox preview
    msg.set_content("Someone is at your front door.")

    # Create a unique string suitable for an RFC 2822-compliant Message-ID header => defaults to domain name (@AV70211.ad.calvin.edu)
    cid = make_msgid()[1:-1]                # removes the <> around the string

    # Attaches HTML alternative to multipart message
    msg.add_alternative(
        '<img src="cid:{cid}" alt="{alt}"/>'
        .format(cid=cid, alt=html.escape(title, quote=True)),
        subtype='html')

    # Guesses the type of the image to send (.png, .jpg, et cetera)
    maintype, subtype = mimetypes.guess_type(str(path))[0].split('/', 1)
    msg.get_payload()[1].add_related(  # image/png
        path.read_bytes(), maintype, subtype, cid="<{cid}>".format(cid=cid))

    try:
        server = smtplib.SMTP_SSL(GMAIL_SERVER, GMAIL_PORT)
        server.ehlo()                   # Open connection to server
        server.login(GMAIL_USER, GMAIL_PASS)        # Login to Gmail account
        server.sendmail(GMAIL_USER, sent_to, msg.as_string())
        server.close()                  # Close connection to server
        print('Email sent to Gmail!')
    except:
        print("Email failed to send.")

# Function to take a picture and store it
def take_pic():
    global camera
    time.sleep(3)
    now = datetime.now()
    nowFormatted = now.strftime("%Y%m%d-%H%M")
    imgName = nowFormatted + ".jpg"
    print("Say cheese!")                                    # **** FOR DEBUGGING ****
    camera.capture(imgName, resize = (432, 324))            # Reduces size of image by factor of 6
    send_email(now, imgName)
    os.remove(imgName)
    print("Image removed!")                                 # **** FOR DEBUGGING ****


# Callback function when doorbell button is pressed
def doorbell_callback(channel):
    take_pic()                  # Take picture
    time.sleep(1)

# Callback function when motion sensor is activated
def motion_callback(channel):
    print("Motion detected.")
    GPIO.output(LED, True)
    startTime = time.time()

    while(GPIO.input(LED) == True):
        if (time.time() - startTime) > 5:
            GPIO.output(LED, False)


# if doorbell button pressed
GPIO.add_event_detect(DOORBELL, GPIO.FALLING, callback=doorbell_callback, bouncetime=1000) 

# if motion sensor activated
GPIO.add_event_detect(MOTION_SENSOR, GPIO.FALLING, callback=motion_callback, bouncetime=300)


# Setup servo motor (lock/unlock)
pi = pigpio.pi()            #connect to pigpiod
if not pi.connected:        #test connection
    exit(0)
pi.set_servo_pulsewidth(MOTOR, 0)

def unlock_door():
    print('Unlocking door')
    pi.set_servo_pulsewidth(MOTOR, UNLOCKPOSITION)

def lock_door():
    print('Locking door')
    pi.set_servo_pulsewidth(MOTOR, LOCKPOSITION)


# Client-Broker Setup
def on_connect(client, userdata, rc, *extra_params):
    print('Connected with result code='+str(rc))

def on_message(client, data, msg):
    if msg.topic == "bdr22/door":
        if str(msg.payload) == VALIDUNLOCK:
            unlock_door()
        if str(msg.payload) == VALIDLOCK:
            lock_door()

# Setup MQTT client and callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username="cs300", password="safeIoT")
client.tls_set('/etc/ssl/certs/ca-certificates.crt')

# Connect to MQTT broker and subscribe to the button topic
client.connect(BROKER, PORT, 60)
client.subscribe("bdr22/door")
client.loop_start()

client.loop_start()
while True: #continuously run
    time.sleep(TIMEBUFFER)

# If you do want to turn it off...
print("Done")
client.disconnect()
camera.close()
GPIO.cleanup() # clean up GPIO
