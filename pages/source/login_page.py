from pages.base_page import BasePage
from datetime import datetime
from config import SOURCE_DOMAIN


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"https://{SOURCE_DOMAIN}/auth/login"

    locators = {
        'email': "input[name='email']",
        'password': "input[name='password']",
        'submit_btn': "button[type='submit']",
        'captcha_iframe': "iframe[title='reCAPTCHA']",
        'captcha_response': "textarea#g-recaptcha-response"
    }

    def open_login_page(self):
        current_time = datetime.now().strftime('%a %d %b %Y')
        self.bypass_cloudflare_check(self.url)
        self.notify(f"✅ Login page was opened. Time: {current_time}")

    def login(self, email, password):
        self.open_login_page()
        self.sb.update_text(self.locators['email'], email)
        self.sb.update_text(self.locators['password'], password)
        self.sb.click(self.locators['submit_btn'])

        if self.sb.is_element_present(self.locators['captcha_iframe']):
            self.notify("⚠️ Captcha found on the page")

            captcha_solution = self.captcha_solver.solve_google_captcha(
                site_key=self.sb.get_attribute(self.locators['captcha_iframe'], "data-sitekey"),
                site_url=self.url
            )
            self.notify(f"✅ Captcha solved: {captcha_solution}")

            self.set_captcha_response(captcha_solution)
            self.sb.click(self.locators['submit_btn'])
        else:
            self.notify("✅ Login success")

    def set_captcha_response(self, captcha_solution):
        if self.sb.is_element_present(self.locators['captcha_response']):
            self.sb.execute_script(f"document.querySelector('{self.locators['captcha_response']}').value='{captcha_solution}';")
        else:
            self.notify("⚠️ Captcha response element not found!")