# pages/sign_up_page.py
import time

from config import SOURCE_DOMAIN
from pages.base_page import BasePage
from email_service.email_handler import get_source_registration_verification_code as get_code

class SignUpPage(BasePage):
    URL = f"https://{SOURCE_DOMAIN}/welcome/signup/e804c47574f73528"

    locators = {
        'username': "input[name='username']",
        'email': "input[name='email']",
        'password': "input[name='password']",
        're_password': "input[name='repassword']",
        'verification_code': "input[name='code']",
        'submit_btn': "button[type='submit']",
    }

    def __init__(self, sb):
        super().__init__(sb)

    def open_signup_page(self):
        self.sb.open(self.URL)

    def register_new_user(self, email, password, user_name):
        self.open_signup_page()

        self.sb.update_text(self.locators['username'], user_name)
        self.sb.update_text(self.locators['email'], email)
        self.sb.update_text(self.locators['password'], password)
        self.sb.update_text(self.locators['re_password'], password)

        self.sb.click(self.locators['submit_btn'])

        self.sb.wait_for_element_visible(self.locators['email'], timeout=10)
        self.sb.update_text(self.locators['email'], email)

        time.sleep(10)
        verification_code = get_code()
        self.sb.update_text(self.locators['verification_code'], verification_code)

        self.sb.click(self.locators['submit_btn'])
        self.sb.sleep(5)

        # todo implement message of a created user in telegram
        print(f"Email: {email}\n"
              f"Password: standard user password\n"
              f"Username: {user_name}\n"
              f"Verification Code: {verification_code}")