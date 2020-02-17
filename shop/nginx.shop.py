[program:course]
command=/home/a0212843/venv/bin/gunicorn config.wsgi:application -c /home/a0212843/CourseDjango2/config/gunicorn.conf.py
directory=/home/a0212843/CourseDjango2
user=a0212843
autorestart=true
redirect_stderr=true
stdout_logfile = /home/a0212843/CourseDjango2/logs/debug.log