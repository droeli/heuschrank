# Howto

`sudo python hs.py`

* development bad practices ignorieren
* freuen über buttons auf port 80 

## Was macht was?

* hs.py: Flask Webapp, Buttons für manuelles auslösen + Zeiten setzen
* switch.py: Auslösen des Relay, als modul oder script
* admin_ops.py: lesen/schreiben von files, cronjobs einrichten
* templates/index.html: Struktur der Website

## Configs:

* channels.json: Welches "relay" an welches GPIO
* timeset.json: Welches "tray" wird um welche Zeit ausgelöst?
* tray_to_relay.json: Welches "tray" ist mit welchem relay verbunden## Configs:

* channels.json: Welches "relay" an welches GPIO
* timeset.json: Welches "tray" wird um welche Zeit ausgelöst?
* tray_to_relay.json: Welches "tray" ist mit welchem relay verbunden?

Tipps:

bluetoothctl
pactl list sinks short
pactl set-sink-volume 2 100%

