#!/bin/bash

exec gunicorn backend.wsgi:application -b 0.0.0.0:8000 --reload


