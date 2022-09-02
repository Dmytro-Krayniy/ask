#sudo unlink /etc/nginx/sites-enabled/default
#sudo ﻿ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ﻿ln -sf /home/mit/PycharmProjects/stepik_django_project/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#sudo gunicorn -w 1 -c /home/box/web/etc/gunicorn.conf.py hello:app
#sudo gunicorn -w 3 -c /home/box/web/etc/gunicorn-django.conf.py ask.wsgi:application
sudo gunicorn -w 1 -c /home/mit/PycharmProjects/stepik_django_project/etc/gunicorn.conf.py hello:app
sudo gunicorn -w 3 -c /home/mit/PycharmProjects/stepik_django_project/etc/gunicorn-django.conf.py ask.wsgi:application


sudo /etc/init.d/gunicorn restart
#﻿sudo /etc/init.d/mysql start﻿



