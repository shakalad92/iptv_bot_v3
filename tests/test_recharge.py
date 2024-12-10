from config import ADMIN_USERNAME, ADMIN_PASSWORD, USER_PASSWORD

from pages.source.login_page import LoginPage
from pages.source.money_transfer_page import MoneyTransferPage
from pages.source.tariff_page import TariffPage
from pages.source.overview_page import OverviewPage


def test_recharge_user(email, amount, sb):
    # Login as Admin
    login_page = LoginPage(sb)
    login_page.login(email=ADMIN_USERNAME, password=ADMIN_PASSWORD)

    # Transfer money to the user
    money_transfer_page = MoneyTransferPage(sb)
    money_transfer_page.recharge_account(email, amount)

    # Check Admin balance and logout
    overview_page = OverviewPage(sb)
    overview_page.check_balance()
    overview_page.logout_source()

    # Login as recharged user #
    login_page.login(email=email, password=USER_PASSWORD)

    # Activate tariff and auto-renewal
    tariff_page = TariffPage(sb)
    tariff_page.activate_tariff()

