import RPi.GPIO as GPIO
import time

channel = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

GPIO.output(channel, GPIO.HIGH)
time.sleep(4)
GPIO.output(channel, GPIO.LOW)
GPIO.cleanup()
