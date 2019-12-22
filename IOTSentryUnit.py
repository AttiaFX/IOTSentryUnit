from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause
from urllib.request import urlopen
import urllib.request
import urllib.request as urllib2
import json
import time

pir = MotionSensor(4)
camera = PiCamera()
WRITE_API_KEY = 'KWW537TZ8A99FVJJ'

baseRL = 'https://api.thingspeak.com/update?api_key=KWW537TZ8A99FVJJ'

camera.start_preview()
frame = 1
while True:
    if pir.wait_for_motion():
        print("Intruder Detected!")
        camera.capture('/home/pi/frame%03d.jpg' % frame)
        print("Photo Taken..")
        frame += 1
        print("Pushing data to ThingSpeak via:")
        print(baseRL + '&field1=%s' % (frame))
        sleep(5)
        conn = urllib.request.urlopen(baseRL + '&field1=%s' % (frame))
        print(conn)
        print(conn.read())
        conn.close()
