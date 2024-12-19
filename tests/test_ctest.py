import random
import string

from config import USER_EMAIL_PREFIX, USER_PASSWORD

from pages.source.signup_page import SignUpPage as SourceSignupPage
from pages.source.login_page import LoginPage
from pages.source.channel_groups_page import ChannelGroupsPage
from pages.source.playlist_page import PlayListPage
from pages.source.tariff_page import TariffPage

from pages.player.signup_page import SignUpPage as PlayerSignupPage
from pages.player.login_page import LoginPage as PlayerLoginPage
from pages.player.playlist_page import PlaylistPage as PlayerPlaylistPage

def test_create_user(phone_number, amount, sb):
    # Prepare user_data
    new_user_email: str = f"{USER_EMAIL_PREFIX}{phone_number}@gmail.com"
    user_name: str = ''.join(random.choices(string.ascii_letters, k=6)).lower()
    user_password: str = USER_PASSWORD

    # Register as new user source
    signup_page = SourceSignupPage(sb)
    signup_page.register_new_user(email=new_user_email, password=user_password, user_name=user_name)

    # Login as new user
    login_page = LoginPage(sb)
    login_page.login(email=new_user_email, password=USER_PASSWORD)

    # Config new user's channel group
    channel_group_page = ChannelGroupsPage(sb)
    channel_group_page.config_playlist()

    # Activate tariff
    tariff_page = TariffPage(sb)
    tariff_page.activate_tariff()

    # Get playlist link and logout
    playlist_page = PlayListPage(sb)
    playlist_link: str = playlist_page.get_playlist_link()

    # Register as new user player
    signup_page = PlayerSignupPage(sb)
    signup_page.register_new_user(email=new_user_email, password=user_password, username=user_name)

    # Login as new user player
    login_page = PlayerLoginPage(sb)
    login_page.login(email=new_user_email, password=user_password)

    # Add playlist and go to settings page
    playlist_page = PlayerPlaylistPage(sb)
    playlist_page.create_playlist(playlist_link, playlist_name="IPTV")


