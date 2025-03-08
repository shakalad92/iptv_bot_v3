import time

from captcha.captcha_solver import CaptchaSolver
from config import (
    SOURCE_DOMAIN,
    TELEGRAM_TOKEN,
    TELEGRAM_CHAT_ID,
    JS_INTERCEPT
)
from message_handler.telegram_message_handler import TelegramMessageHandler


class BasePage:
    def __init__(self, driver):
        self.sb = driver
        self._bot = TelegramMessageHandler(token=TELEGRAM_TOKEN, chat_id=TELEGRAM_CHAT_ID)
        self.captcha_solver = CaptchaSolver()

    def logout_source(self) -> None:
        self.sb.get(f"https://{SOURCE_DOMAIN}/auth/signout")
        self.notify("✅ YOU HAVE LOGGED OUT")

    def bypass_cloudflare_check(self, url):
        self.sb.get("about:blank")
        self.sb.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": JS_INTERCEPT})
        self.sb.uc_open_with_reconnect(url, 4)
        self.sb.uc_gui_click_captcha()

        captcha_params = self.get_captcha_params()
        if not captcha_params:
            self.notify("❌ Cloudflare captcha NOT FOUND")
            raise Exception("Cloudflare captcha NOT FOUND")

        solution = self.captcha_solver.solve_turnstile_captcha(url, captcha_params)

        self.sb.execute_script(f'window.tsCallback("{solution}");')
        self.notify("✅ Cloudflare SUCCESSFULLY PASSED")

        self.sb.uc_gui_click_captcha()

    def get_captcha_params(self, retries=20, delay=1):
        for _ in range(retries):
            captcha_params = self.sb.execute_script("return window.captchaParams;")
            if captcha_params:
                return captcha_params
            time.sleep(delay)
        return None

    def notify(self, message: str) -> None:
        self._bot.send_message(message=message)

    def open_main_page(self):
        self.sb.get(f"https://{SOURCE_DOMAIN}/cabinet")
        time.sleep(3)