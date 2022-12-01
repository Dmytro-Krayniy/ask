git clone --branch path https://github.com/Dmytro-Krayniy/ask.git /home/box/web/ask

﻿#sudo unlink /etc/nginx/sites-enabled/default
#sudo ﻿ln -sf /home/box/web/ask/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ﻿ln -sf /home/mit/PycharmProjects/ask/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#sudo gunicorn -w 1 -c /home/box/web/ask/etc/gunicorn.conf.py hello:app &
#sudo gunicorn -c /home/box/web/ask/etc/gunicorn-django.conf.py ask.wsgi:application &
sudo gunicorn -w 1 -c /home/mit/PycharmProjects/ask/etc/gunicorn.conf.py hello:app &
sudo gunicorn -w 3 -c /home/mit/PycharmProjects/ask/etc/gunicorn-django.conf.py ask.wsgi:application &

sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql start﻿
mysql -uroot -e "create database stepic_web;"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate


На локальной машине я отлаживался в Django 1.9
В процессе отладки столкнулся с проблемой что модели не применяются к базе данных.
Чтобы это побороть я использовал команду
python manage.py makemigrations qa

﻿После этого использовал команду
python manage.py migrate


# остановить полностью все workers of gunicorn sudo pkill -f gunicorn

Итак, путем проб и ошибок удалось выяснить, что перед скачиванием своего репозитория, необходимо выполнить следующие команды:

sudo apt update
sudo apt install python3.5
sudo apt install python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install gunicorn
sudo python3 -m pip install django==2.0
sudo python3 -m pip install mysqlclient



python3 manage.py runserver 0.0.0.0:8000

Чтобы начать пользоваться виртуальным окружением, необходимо его активировать:
source venv/bin/activate

