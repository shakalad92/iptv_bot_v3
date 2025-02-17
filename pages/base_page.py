import time

from config import SOURCE_DOMAIN
class BasePage:
    def __init__(self, driver):
        self.sb = driver

    def logout_source(self):
        self.sb.get(f"https://{SOURCE_DOMAIN}/auth/signout")

    def open_main_page(self):
        self.sb.get(f"https://{SOURCE_DOMAIN}/cabinet")
        time.sleep(3)