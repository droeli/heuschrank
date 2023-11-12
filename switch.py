import RPi.GPIO as GPIO
import sys
import time
from admin_ops import write_timeset, load_json, refresh_cron

def turnon(relay):
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(relay, GPIO.OUT)
  GPIO.output(relay, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(relay, GPIO.LOW)
  GPIO.cleanup()

if __name__ == "__main__":
  channels = load_json('/home/droeli/heuschrank/channels.json')
  turnon(channels[sys.argv[1]])
  print('turned on',sys.argv[1],'for 2 seconds')
