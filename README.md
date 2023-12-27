# Howto

## Erstes Setup:

Für jedes Relay (Auslöser) muss ein wav Audio File in den Ordner /home/hs/heuschrank abgelegt werden: rel_one.wav, rel_two.wav, rel_three.wav

Die wav Dateien *müssen* ein 16-bit PCM encoding mit 44100Hz Sample Rate haben. Je nach Speaker 1-2 Sekunden Stille vorne reinschneiden damit nichts verschluckt wird.

```
cd /home/hs/heuschrank
vi connect_speaker.sh # Hier MAC Adresse des Bluetooth Speaker eintragen! Siehe Tipps
cd /home/hs/heuschrank/install
./install.sh
```

## Start
### Manuell für Testing
`python3 hs.py`

### Produktiv
`sudo systemctl start heuschrank`

## Operation
Nach der Installation ist kein automatisches öffnen konfiguriert. Dazu auf http://<name_des_schranks:8080 im WLAN gehen und in die Textboxen Zeiten eintragen (z.B: 15:30).

Das entsprechende Fach öffnet sich dann jeden Tag um diese Uhrzeit.

Oder einfach mit den Knöpfen "Top, Middle, Bottom" die Fächer manuell auslösen und freuen :)

## Was macht was?

* hs.py: Flask Webapp, Buttons für manuelles auslösen + Zeiten setzen
* switch.py: Script um Audio abzuspielen und turnon admin op aufzurufen (benutzt von Cron)
* admin_ops.py: lesen/schreiben von configs, cronjobs einrichten, relay auslösen (von anderen scripten via subprocess als root gestartet)
* connect_speaker.sh: Disconnect/Connect vom Speaker beim Start um billige Bluetooth speaker zu unterstützen die nicht sauber auto-connecten.
* install/install.sh: Installieren des systemd service (für automatischen start im Hintergrund und nach reboot)
* install/heuschrank.service: Systemd Unit file für Service
* templates/index.html: Struktur der Website

## Configs:

* channels.json: Welches "relay" an welches GPIO
* timeset.json: Welches "tray" wird um welche Zeit ausgelöst? (wird erst durch den Button 'Set Times' in der Weboberfläche festgeschrieben)
* tray_to_relay.json: Welches "tray" ist mit welchem relay verbunden

## Tipps:

### bluetoothctl

Mit bluethoothctl kann nach einem Bluetooth speaker gesucht werden. Ablauf ist:
```
scan
connect MAC
pair MAC
trust MAC
```

### Speaker Volume
pactl list sinks short
pactl set-sink-volume 2 100%

