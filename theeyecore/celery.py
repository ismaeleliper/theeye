import os
from theeyecore import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theeyecore.settings')

app = Celery("theeyecore")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def create(x, y):
    return x + y


@app.task
def create_new_session(request):
    from api.models import UserSession
    return UserSession.objects.create(
        category=request['category'],
        name=request['name'],
        data=request['data']
    )


