from config import USER_PASSWORD
from pages.player.playlist_page import PlaylistPage
from pages.player.signup_page import SignUpPage
from pages.player.login_page import LoginPage


def test_create_account(email, sb):
    playlist_link = "http://31a92883d51b.faststreem.org/playlists/uplist/520980bdcc09720a6783ab19b746e728/playlist.m3u8"

    signup_page = SignUpPage(sb)
    signup_page.register_new_user(email=email, password=USER_PASSWORD, username="mbananamama")

    # Login as new user player
    login_page = LoginPage(sb)
    login_page.login(email=email, password=USER_PASSWORD)

    # Add playlist and go to settings page
    playlist_page = PlaylistPage(sb)
    playlist_page.create_playlist(playlist_link, playlist_name="IPTV")