# pages/sign_up_page.py
import time

from config import PLAYER_DOMAIN
from pages.base_page import BasePage
from email_service.email_handler import get_player_registration_activation_link

class SignUpPage(BasePage):
    URL = f"https://{PLAYER_DOMAIN}/account/registration"

    locators = {
        'username': "input[name='username']",
        'email': "input[name='email']",
        'password': "input[name='password']",
        're_password': "input[name='repassword']",
        'submit_btn': "button[type='submit']",
    }

    def __init__(self, sb):
        super().__init__(sb)

    def open_signup_page(self):
        self.sb.uc_open_with_reconnect(self.URL, 4)
        self.sb.uc_gui_click_captcha()

    def register_new_user(self, email: str, password: str, username: str) -> None:
        self.open_signup_page()

        self.sb.update_text(self.locators['username'], username)
        self.sb.update_text(self.locators['email'], email)
        self.sb.update_text(self.locators['password'], password)
        self.sb.update_text(self.locators['re_password'],password)

        self.sb.click(self.locators['submit_btn'])

        self.sb.sleep(10)
        activation_link = get_player_registration_activation_link()

        self.sb.open(activation_link)
        print(f"Account activated for email: {email}")
