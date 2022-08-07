# Parsing olx sites


### Installation

```bash
pip3 install -r requirements.txt
```

Also you need download and startup redis

[Install redis](https://redis.io/docs/getting-started/installation/)

### Configure

In file **configs/app_config.py** set credentials for database 

```python
# MYSQL CONNECTION DATA
MYSQL_USER = 'root'

MYSQL_PASSWORD = 'root'

MYSQL_HOST = 'localhost'

MYSQL_PORT = 3306

MYSQL_DATABASE = 'olx'
```

In file **configs/celery_config.py** set credentials for redis
```python
redis_host = '0.0.0.0'

redis_port = '6379'
    
broker_url = 'redis://' + redis_host + ':' + redis_port + '/0'

result_backend = 'redis://' + redis_host + ':' + redis_port + '/0'
```

### Run application

```bash
celery -A celery_parsing worker -l INFO
```

```bash
celery -A celery_parsing beat -l INFO -s celery_parsing/schedule_db/celerybeat-schedule
```