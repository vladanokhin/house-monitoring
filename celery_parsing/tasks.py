from celery_parsing import app
from .browser_parser import OlxParser
from .telethon_client import TelegramBot


@app.task(retries=3, default_retry_delay=1)
def parse_olx():
    olx = OlxParser()
    houses = olx.search_new_houses()
    olx._browser.quit()

    if len(houses) > 0:
        client = TelegramBot()
        msg = olx.prepare_message(houses)
        client.notification_users(msg)

