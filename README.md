# Raspserver
Raspberry Pi server project

#RPi Setup
There are two run files. run_dev.py enables debugging and runs only on the localhost. run_prod.py disables debugging and runs openly on the network.

Run server automatically from cron:

crontab -e

add: @reboot raspserver/flask/bin/python raspserver/run_prod.py

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

#Platform Setup
Place admin usernames in file admins.txt in the main folder (eg. ['John','Bob'] ). These usernames will automatically be granted admin privileges when an account with that name is created. Be careful to make this account when setting up the system, otherwise an admin account is up for grabs.