# Raspserver
Raspberry Pi server project

# RPi setup
Add pull.sh to crontab to enable automatic updating from master:

0 * * * * /usr/bin/sudo - H /home/pi/raspserver/pull.sh >> /dev/null 2>&1

# Flask setup
Run virtualenv.py: python virtualenv.py flask

Requirements: pip install flask