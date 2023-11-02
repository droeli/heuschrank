import RPi.GPIO as GPIO
import time
from flask import Flask, render_template

channel = {
  'lock': 17,
  'magnet': 27
}

app = Flask(__name__)

def turnon(relay):
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(channel[relay], GPIO.OUT)
  GPIO.output(channel[relay], GPIO.HIGH)
  time.sleep(2)
  GPIO.output(channel[relay], GPIO.LOW)
  GPIO.cleanup()

@app.route('/')
def index():
  return render_template('index.html', infotext='Press a button!')

@app.route('/<relay>/on')
def goon(relay):
  turnon(relay)
  return render_template('index.html', infotext='turned on ' + relay)


app.run(host='0.0.0.0', port=80)

