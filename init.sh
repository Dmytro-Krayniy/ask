#!/bin/bash

sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/ask/etc/nginx.conf /etc/nginx/sites-enabled/default
#sudo ﻿ln -sf /home/mit/PycharmProjects/ask/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo /etc/init.d/mysql restart﻿
mysql -uroot -e "create database stepic_web;"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"

#source venv/bin/activate
sudo python3 -m pip install django==2.0

python3 manage.py makemigrations
python3 manage.py migrate

#sudo gunicorn -w 1 -c /home/box/web/ask/etc/gunicorn.conf.py hello:app &
sudo gunicorn -c /home/box/web/ask/etc/gunicorn-django.conf.py ask.wsgi:application &

#sudo /etc/init.d/gunicorn restart
# остановить полностью все workers of gunicorn sudo pkill -f gunicorn




