import json
import RPi.GPIO as GPIO
import subprocess
import time
from admin_ops import write_timeset, load_json, refresh_cron
from flask import Flask, render_template, request
#from switch import turnon

channel = load_json('/home/hs/heuschrank/channels.json')

GPIO.setmode(GPIO.BCM)

unlock_times = load_json('/home/hs/heuschrank/timeset.json')

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', infotext='Manually release a lock or change times', unlock_times=unlock_times)

@app.route('/<relay>/on')
def goon(relay):
  subprocess.run(['/usr/bin/python3', 'switch.py', relay])
  return render_template('index.html', infotext='turned on ' + relay, unlock_times=unlock_times)

@app.route('/settime/', methods=['POST'])
def settime():
  time_top = request.form['time_top']
  time_middle = request.form['time_middle']
  time_bottom = request.form['time_bottom']
  unlock_times = {
    "time_top": time_top,
    "time_middle": time_middle,
    "time_bottom": time_bottom
  }
  write_timeset(unlock_times)
  subprocess.run(['/usr/bin/sudo', '/usr/bin/python3', 'admin_ops.py', 'refresh_cron'])
  return render_template('index.html', infotext='Times set!', unlock_times=unlock_times)
  


app.run(host='0.0.0.0', port=8080)
GPIO.cleanup()
