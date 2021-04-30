#! /usr/bin/env sh

/usr/sbin/crond
python manage.py migrate
python manage.py crontab add
gunicorn youtube_videos.wsgi -b 0.0.0.0:8000