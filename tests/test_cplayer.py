from config import USER_PASSWORD
from pages.player.playlist_page import PlaylistPage
from pages.player.signup_page import SignUpPage
from pages.player.login_page import LoginPage

import string, random

def test_create_player(email, playlist_link, sb):
    username: str = ''.join(random.choices(string.ascii_letters, k=6)).lower()

    # Register new user
    signup_page = SignUpPage(sb)
    signup_page.register_new_user(email=email, password=USER_PASSWORD, username=username)

    # Login as new user player
    login_page = LoginPage(sb)
    login_page.login(email=email, password=USER_PASSWORD)

    # Add playlist and go to settings page
    playlist_page = PlaylistPage(sb)
    playlist_page.create_playlist(playlist_link=playlist_link, playlist_name="IPTV")