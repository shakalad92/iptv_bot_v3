# pages/login_page.py
from config import PLAYER_DOMAIN
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = f"https://{PLAYER_DOMAIN}/account/login"

    locators = {
        'email': "input[name='email']",
        'password': "input[name='password']",
        'submit_btn': "button[type='submit']",
    }

    def __init__(self, sb):
        super().__init__(sb)

    def open_login_page(self):
        self.sb.uc_open_with_reconnect(self.URL, 4)
        self.sb.uc_gui_click_captcha()

    def login(self, email, password):
        self.open_login_page()
        self.sb.sleep(2)
        self.sb.update_text(self.locators['email'], email)
        self.sb.update_text(self.locators['password'], password)
        self.sb.click(self.locators['submit_btn'])
        print(f"Logged in as: {email}")