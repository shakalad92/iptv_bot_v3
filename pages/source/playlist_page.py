# pages/play_list_page.py
from config import SOURCE_DOMAIN
from pages.base_page import BasePage

class PlayListPage(BasePage):
    URL = f"https://{SOURCE_DOMAIN}/playlist/download"

    locators = {
        'playlist_link': "div[id='pllink']",
        'playlist_download': "button[id='setFileType']"
    }

    def __init__(self, sb):
        super().__init__(sb)

    def open_playlist_page(self):
        self.sb.open(self.URL)

    def get_playlist_link(self):
        self.open_playlist_page()
        self.notify("Playlist page was opened")
        self.sb.wait_for_element_visible(self.locators['playlist_link'], timeout=10)
        playlist_link = self.sb.get_text(self.locators['playlist_link'])

        self.notify(f"Playlist was created. Link: {playlist_link}")

        return playlist_link