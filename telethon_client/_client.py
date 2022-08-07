from os import getenv
from telethon import TelegramClient
from telethon import events

from configs import Config

cfg = Config()

client = TelegramClient(
    cfg.SESSION_NAME,
    cfg.APP_ID,
    cfg.APP_HASH
)
