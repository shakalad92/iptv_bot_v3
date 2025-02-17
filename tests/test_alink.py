from config import USER_PASSWORD
from pages.player.playlist_page import PlaylistPage
from pages.player.login_page import LoginPage

def test_add_playlist_link(email, playlist_link, sb):
    # Login as new user player
    login_page = LoginPage(sb)
    login_page.login(email=email, password=USER_PASSWORD)

    # Add playlist and go to settings page
    playlist_page = PlaylistPage(sb)
    playlist_page.create_playlist(playlist_link=playlist_link, playlist_name="IPTV")