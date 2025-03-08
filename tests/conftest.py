# conftest.py
import pytest
from seleniumbase import SB


def pytest_addoption(parser):
    parser.addoption("--email", action="store", help="Email for the test")
    parser.addoption("--amount", action="store", help="Amount for the test")
    parser.addoption("--phone_number", action="store", help="Phone number for the test")
    parser.addoption("--playlist_link", action="store", help="Playlist link for the test")


@pytest.fixture
def email(request):
    return request.config.getoption("--email")


@pytest.fixture
def amount(request):
    return request.config.getoption("--amount")

@pytest.fixture
def phone_number(request):
    return request.config.getoption("--phone_number")

@pytest.fixture
def playlist_link(request):
    return request.config.getoption("--playlist_link")


@pytest.fixture
def sb():
    with SB(uc=True, locale="en") as sb:
        sb.maximize_window()
        yield sb
