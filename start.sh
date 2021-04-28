#! /usr/bin/env sh

/usr/sbin/crond
python manage.py crontab add
python manage.py migrate
gunicorn youtube_videos.wsgi -b 0.0.0.0:8000