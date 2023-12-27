import jinja2
import json
import RPi.GPIO as GPIO
import sys
import time

def write_timeset(unlock_times):
  with open('/home/hs/heuschrank/timeset.json', 'w') as timeset_file:
    json.dump(unlock_times, timeset_file, indent=4)

def load_json(filename):
  with open(filename) as jsonfile:
    return json.load(jsonfile)

def refresh_cron():
  environment = jinja2.Environment()
  cron_template = """
XDG_RUNTIME_DIR=/run/user/1000
{% for relay, hour, minute in activation_times %}
{{ minute }} {{ hour }} * * * hs /usr/bin/python3 /home/hs/heuschrank/switch.py {{ relay }}
{% endfor %}
"""
  template = environment.from_string(cron_template)
  timeset = load_json('/home/hs/heuschrank/timeset.json')
  tray_to_relay = load_json('/home/hs/heuschrank/tray_to_relay.json')
  activation_times = []
  for timedesc, time in timeset.items():
    relay = tray_to_relay[timedesc.replace('time_','')]
    hour, minute = time.split(':')
    activation_times.append([relay, hour, minute])
  with open('/etc/cron.d/heuschrank', 'w') as cronfile:
    cronfile.write(template.render(activation_times=activation_times))

def turnon(relay):
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(relay, GPIO.OUT)
  GPIO.output(relay, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(relay, GPIO.LOW)
  GPIO.cleanup()

if __name__ == "__main__":
    if sys.argv[1] == 'refresh_cron':
        refresh_cron()

    if sys.argv[1] == 'turnon':
        turnon(int(sys.argv[2]))
