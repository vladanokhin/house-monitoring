from celery import Celery
from configs import CeleryConfig

# celery -A celery_parsing worker -l INFO
app = Celery('celery_parsing')

app.config_from_object(CeleryConfig)

app.autodiscover_tasks(['celery_parsing'])
