

exec gunicorn backend_setting.wsgi:application -b 0.0.0.0:8000 --reload