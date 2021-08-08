from .celery import app as celery_app
from .mqtt import mqtt

__all__ = ('celery_app',)
mqtt.client.loop_start()