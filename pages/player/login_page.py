from config import PLAYER_DOMAIN, CAPTCHA_URL
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = {
        'email': "input[name='email']",
        'password': "input[name='password']",
        'submit_btn': "button[type='submit']",
    }

    def __init__(self, sb):
        super().__init__(sb)
        self.url = f"https://{PLAYER_DOMAIN}/account/login"

    def open_login_page(self):
        self.bypass_cloudflare_check(CAPTCHA_URL)
        self.notify("✅ Player Login page was opened")

    def login(self, email, password):
        self.open_login_page()
        self.sb.sleep(2)
        self.sb.update_text(self.locators['email'], email)
        self.sb.update_text(self.locators['password'], password)
        self.sb.click(self.locators['submit_btn'])
        self.notify(f"✅ Logged in as: {email}")