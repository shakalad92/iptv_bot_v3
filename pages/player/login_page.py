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
        self.sb.open(self.URL)

    def login(self, email, password):
        self.open_login_page()
        self.notify("Player Login page was opened")
        self.sb.sleep(2)
        self.sb.update_text(self.locators['email'], email)
        self.sb.update_text(self.locators['password'], password)
        self.sb.click(self.locators['submit_btn'])

        self.notify(f"Logged in as: {email}")