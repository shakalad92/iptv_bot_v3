from config import SOURCE_DOMAIN
from pages.base_page import BasePage


class TariffPage(BasePage):
    URL = f"https://{SOURCE_DOMAIN}/tariff/info"

    locators = {
        'activation_btn': "button#actTariffBtn",
        'auto_renewal_btn': "button#actAutoBtn",
    }

    def __init__(self, sb):
        super().__init__(sb)

    def try_click_button(self, button_locator):
            if self.sb.wait_for_element_clickable(button_locator, timeout=10):
                self.sb.click(button_locator)
                self.notify(f"{button_locator} button was clicked")
            else:
                self.notify(f"{button_locator} button is not active")

    def open_tariff_page(self):
        self.sb.open(self.URL)

    def activate_tariff(self):
        self.open_tariff_page()
        self.try_click_button(self.locators['activation_btn'])
        self.try_click_button(self.locators['auto_renewal_btn'])
