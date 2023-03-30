import sys
import os
from celery import Celery
from configs import CeleryConfig


# Adding the 'src' directory to the python path
sys.path.insert(0, os.path.join(os.getcwd(), 'app'))

app = Celery('celery_parsing')

app.config_from_object(CeleryConfig)

app.autodiscover_tasks(['celery_parsing'])
