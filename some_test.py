from seleniumbase import SB

from config import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN
from message_handler.telegram_message_handler import TelegramMessageHandler

with SB(uc=True, test=True, locale="en") as sb:
    url = "https://vipdrive.net"
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()

    telegram = TelegramMessageHandler(token=TELEGRAM_TOKEN, chat_id=TELEGRAM_CHAT_ID)
    telegram.send_message("sexxxxxxxxx")

    sb.sleep(2)
