import jinja2
import json

cron_template="""
{{% for relay, hour, minute in activation_times %}
{{ minute }} {{ hour }} * * * sudo /home/droeli/heuschrank/switch.py {{ relay }}
{% endfor %}
"""

def write_timeset(unlock_times):
  with open('/home/droeli/heuschrank/timeset.json', 'w') as timeset_file:
    json.dump(unlock_times, timeset_file, indent=4)

def load_json(filename):
  with open(filename) as jsonfile:
    return json.load(jsonfile)

def refresh_cron():
  environment = jinja2.Environment()
  cron_template = """
{% for relay, hour, minute in activation_times %}
{{ minute }} {{ hour }} * * * root /usr/bin/python /home/droeli/heuschrank/switch.py {{ relay }} >> /home/droeli/heuschrank/activity.log 2>&1
{% endfor %}
"""
  template = environment.from_string(cron_template)
  timeset = load_json('/home/droeli/heuschrank/timeset.json')
  tray_to_relay = load_json('/home/droeli/heuschrank/tray_to_relay.json')
  activation_times = []
  for timedesc, time in timeset.items():
    relay = tray_to_relay[timedesc.replace('time_','')]
    hour, minute = time.split(':')
    activation_times.append([relay, hour, minute])
  with open('/etc/cron.d/heuschrank', 'w') as cronfile:
    cronfile.write(template.render(activation_times=activation_times))
