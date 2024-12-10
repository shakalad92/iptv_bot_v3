# pages/money_transfer_page.py
import time

from email_service.email_handler import get_transaction_verification_code
from pages.base_page import BasePage

from config import SOURCE_DOMAIN


class MoneyTransferPage(BasePage):
    URL = f"https://{SOURCE_DOMAIN}/finance/moneytransfer"

    locators = {
        "recipient_email": "input[name='email']",
        "trans_amount": "input[id='mTransAmount']",
        "confirmation_method": "select[name='code_transport']",
        "trans_submit_btn": "button[id='mTransBtn']",
        "verification_code": "input[name='code']",
        "submit_btn": "button[type='submit']",
        "warning_message": "div.uk-notification-message.uk-notification-message-warning",
    }

    def __init__(self, sb):
        super().__init__(sb)

    def open_money_transfer_page(self):
        self.sb.open(self.URL)

    def recharge_account(self, email, amount):
        self.transfer_money_to_the_user(email, amount)

    def transfer_money_to_the_user(self, email, amount="1"):
        self.open_money_transfer_page()

        self.sb.select_option_by_value(self.locators["confirmation_method"], "email")
        self.sb.update_text(self.locators["recipient_email"], email)
        self.sb.clear(self.locators["trans_amount"])
        self.sb.update_text(self.locators["trans_amount"], amount)
        self.sb.highlight(self.locators["trans_submit_btn"])
        self.sb.click(self.locators["trans_submit_btn"])
        self.sb.click(self.locators["submit_btn"])

        if self.sb.is_element_visible(self.locators["warning_message"]):
            warning_message = self.sb.get_text(self.locators["warning_message"])
            raise Exception(f"### {warning_message}")

        self.sb.wait_for_element_visible(self.locators["verification_code"], timeout=15)
        time.sleep(10)
        verification_code = get_transaction_verification_code()
        self.sb.update_text(self.locators["verification_code"], verification_code)
        self.sb.click(self.locators["submit_btn"])
        self.sb.sleep(5)
