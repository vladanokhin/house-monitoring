from dotenv import load_dotenv
from os import getenv
from celery.schedules import crontab


class Config:

    def __init__(self):
        load_dotenv()

    @property
    def SESSION_NAME(self):
        return getenv('SESSION_NAME', 'production')

    @property
    def APP_ID(self):
        return getenv('APP_ID', 12345)

    @property
    def APP_HASH(self):
        return getenv('APP_HASH', '12345')

    @property
    def BROWSER_DRIVER(self):
        return getenv('BROWSER_DRIVER', 'driver/chromedriver-macos')

    @property
    def URL_PARSING(self):
        return getenv('URL_PARSING', 'http://google.com/')

    NOTIFICATION_USERS = [
        476489188,
        729407135
    ]


class CeleryConfig:
    redis_host = getenv('REDIS_HOST', '127.0.0.1')

    redis_port = getenv('REDIS_PORT', '6379')

    broker_url = 'redis://' + redis_host + ':' + redis_port + '/0'

    result_backend = 'redis://' + redis_host + ':' + redis_port + '/0'

    task_serializer = 'json'

    result_serializer = 'json'

    accept_content = ['application/json']

    timezone = 'Europe/Kiev'

    enable_utc = True

    worker_max_tasks_per_child = 3

    task_time_limit = 60 * 30  # 30 minutes

    beat_schedule = {
        'test-task': {
            'task': 'celery_parsing.tasks.parse_olx',
            'schedule': crontab(minute='*/3'),
        }
    }