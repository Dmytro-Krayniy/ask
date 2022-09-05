#sudo unlink /etc/nginx/sites-enabled/default
#sudo ﻿ln -sf /home/box/ask/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ﻿ln -sf /home/mit/PycharmProjects/ask/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#sudo gunicorn -w 1 -c /home/box/ask/etc/gunicorn.conf.py hello:app &
#sudo gunicorn -w 3 -c /home/box/ask/etc/gunicorn-django.conf.py ask.wsgi:application &
sudo gunicorn -w 1 -c /home/mit/PycharmProjects/ask/etc/gunicorn.conf.py hello:app &
sudo gunicorn -w 3 -c /home/mit/PycharmProjects/ask/etc/gunicorn-django.conf.py ask.wsgi:application &


sudo /etc/init.d/gunicorn restart
#﻿sudo /etc/init.d/mysql start﻿



