# login_page.py
from captcha.captcha_solver import CaptchaSolver
from pages.base_page import BasePage

from config import CAPTCHA_API_KEY, CAPTCHA_SITE_KEY, CAPTCHA_URL, SOURCE_DOMAIN

from datetime import datetime


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.url = f"https://{SOURCE_DOMAIN}/auth/login"

        self.captcha_api_key = CAPTCHA_API_KEY
        self.captcha_site_key = CAPTCHA_SITE_KEY
        self.captcha_url = CAPTCHA_URL
        self.captcha_solver = CaptchaSolver(
            api_key=self.captcha_api_key,
            site_key=self.captcha_site_key,
            site_url=self.captcha_url)

    locators = {
        'email': "input[name='email']",
        'password': "input[name='password']",
        'submit_btn': "button[type='submit']",
        'captcha_iframe': "iframe[title='reCAPTCHA']"
    }

    def open_login_page(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%a %d %b %Y')
        self.sb.uc_open_with_reconnect(self.url, 4)
        self.sb.uc_gui_click_captcha()

    def login(self, email, password):
        self.open_login_page()

        self.sb.update_text(self.locators['email'], email)
        self.sb.update_text(self.locators['password'], password)
        self.sb.click(self.locators['submit_btn'])

        if self.sb.is_element_present(self.locators['captcha_iframe']):

            self.sb.update_text(self.locators['email'], email)
            self.sb.update_text(self.locators['password'], password)

            captcha_solution = self.captcha_solver.solve_captcha()
            self.set_captcha_response(captcha_solution)

            self.sb.click(self.locators['submit_btn'])

    def set_captcha_response(self, captcha_solution):
        script = f"document.getElementById('g-recaptcha-response').innerHTML='{captcha_solution}';"
        self.sb.execute_script(script)
