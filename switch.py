import RPi.GPIO as GPIO
import subprocess
import sys
import time
from admin_ops import write_timeset, load_json, refresh_cron

if __name__ == "__main__":
  channels = load_json('/home/hs/heuschrank/channels.json')
  subprocess.run(['/usr/bin/python3', '/home/hs/heuschrank/audio.py', sys.argv[1]])
  #turnon(channels[sys.argv[1]])
  subprocess.run(['/usr/bin/sudo', '/usr/bin/python3', '/home/hs/heuschrank/admin_ops.py', 'turnon', str(channels[sys.argv[1]])])
  print('turned on',sys.argv[1],'for 2 seconds')
