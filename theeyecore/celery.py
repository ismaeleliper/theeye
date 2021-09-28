from os import environ
from celery import Celery


environ.setdefault('CELERY_CONFIG_MODULE', 'celery_settings')

app = Celery()
app.config_from_envvar('CELERY_CONFIG_MODULE')


