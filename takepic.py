#!/bin/python

from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera takes a couple of seconds to get ready
sleep(2)
camera.capture('calbal24.jpg')
