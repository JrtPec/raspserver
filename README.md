# Raspserver
Raspberry Pi server project

# RPi setup
Add pull.sh to crontab to enable automatic updating from master:

0 * * * * /usr/bin/sudo - H /home/pi/raspserver/pull.sh >> /dev/null 2>&1

# Flask setup
Run virtualenv.py: python virtualenv.py flask

Requirements:

flask/bin/pip install flask

flask/bin/pip install Flask-login

flask/bin/pip install Flask-SQLalchemy

flask/bin/pip install Flask-WTF

flask/bin/pip install sqlalchemy-migrate==0.9.1

#DB Setup
Run db_create.py when running for the first time, after that use migrate or upgrade scripts when modifying database structure