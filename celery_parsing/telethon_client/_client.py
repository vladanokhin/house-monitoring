from telethon import TelegramClient

from configs import Config


class TelegramBot:

    def __init__(self):
        self.cfg = Config()
        self.client = TelegramClient(
            self.cfg.SESSION_NAME,
            self.cfg.APP_ID,
            self.cfg.APP_HASH
        )
        self.client.start()

    def notification_users(self, message: str) -> None:
        """
        Send message to all users
        :param message: string of message
        :return: None
        """
        for user_id in self.cfg.NOTIFICATION_USERS:
            self.client.loop.run_until_complete(
                self.client.send_message(user_id, message, link_preview=False)
            )
