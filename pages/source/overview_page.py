# pages/overview_page.py
from config import SOURCE_DOMAIN
from pages.base_page import BasePage


class OverviewPage(BasePage):
    URL = f"https://{SOURCE_DOMAIN}/finance/overview"

    locators = {
        "balance": "span.uk-text-lead",
    }

    def __init__(self, sb):
        super().__init__(sb)

    def open_overview_page(self):
        self.sb.open(self.URL)

    def check_balance(self):
        self.open_overview_page()
        self.notify("Overview page was opened")
        self.sb.wait_for_element_visible(self.locators["balance"], timeout=10)

        balance_text = self.sb.get_text(self.locators["balance"])

        self.notify(f"Admin Balance: {balance_text}")