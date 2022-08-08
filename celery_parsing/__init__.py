from celery import Celery
from configs import CeleryConfig

app = Celery('celery_parsing')

app.config_from_object(CeleryConfig)

app.autodiscover_tasks(['celery_parsing'])
