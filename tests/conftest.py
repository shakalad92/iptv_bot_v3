# conftest.py
import pytest
from seleniumbase import SB


def pytest_addoption(parser):
    parser.addoption("--email", action="store", help="Email for the test")
    parser.addoption("--amount", action="store", help="Amount for the test")


@pytest.fixture
def email(request):
    return request.config.getoption("--email")


@pytest.fixture
def amount(request):
    return request.config.getoption("--amount")


@pytest.fixture
def sb():
    with SB(uc=True) as sb:
        sb.maximize_window()
        yield sb
