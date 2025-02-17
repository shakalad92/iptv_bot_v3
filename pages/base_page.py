
import time
from config import SOURCE_DOMAIN, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
from message_handler.telegram_message_handler import TelegramMessageHandler


class BasePage:
    def __init__(self, driver):
        self.sb = driver
        self._bot = TelegramMessageHandler(token=TELEGRAM_TOKEN, chat_id=TELEGRAM_CHAT_ID)

    def logout_source(self) -> None:
        self.sb.get(f"https://{SOURCE_DOMAIN}/auth/signout")
        self.notify("Successfully logged out.")

    def bypass_cloudflare_check(self, url):
        self.sb.uc_open_with_reconnect(url, 4)
        self.sb.uc_gui_click_captcha()

    def notify(self, message: str) -> None:
        self._bot.send_message(message=message)

    def open_main_page(self):
        self.sb.get(f"https://{SOURCE_DOMAIN}/cabinet")
        time.sleep(3)
