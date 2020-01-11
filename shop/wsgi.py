"""
WSGI config for shop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings') # директория и файл настройки нашего проекта

application = get_wsgi_application()

"""
Данный файл позволяет запускать наш проект на вебсервере

Это прослойка между проектом и вебсервером

WSGI (англ. Web Server Gateway Interface) — стандарт взаимодействия между Python-программой, выполняющейся на стороне 
сервера, и самим веб-сервером[1], например Apache.
"""