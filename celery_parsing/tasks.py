from celery_parsing import app


@app.task(retries=3, default_retry_delay=1)
def parse_olx():
    pass
