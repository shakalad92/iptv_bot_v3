# pages/playlist_page.py
import os

from config import PLAYER_DOMAIN
from pages.base_page import BasePage

class PlaylistPage(BasePage):
    URL = f"https://{PLAYER_DOMAIN}/playlist/original"

    locators = {
        'playlist_name': "input[id='plName']",
        'playlist_link_toggle': "div#sources_toggle:nth-child(2)",
        'playlist_link': "input[name='source']",
        'playlist_upload_input': "input#inplaylist",
        'submit_btn': "button[type='submit']",
        'settings_btn': "a[uk-icon='settings']",
        'success_message': "div.uk-notification-message.uk-notification-message-success",
    }

    def __init__(self, sb):
        super().__init__(sb)

    def open_playlist_page(self):
        self.sb.open(self.URL)

    def create_playlist(self, playlist_link: str, playlist_name):
        while True:
            self.open_playlist_page()

            self.sb.update_text(self.locators['playlist_name'], playlist_name)
            self.sb.click(self.locators['playlist_link_toggle'])
            self.sb.update_text(self.locators['playlist_link'], playlist_link)
            self.sb.sleep(2)

            self.sb.click(self.locators['submit_btn'])
            self.sb.sleep(2)

            if self.sb.is_element_visible(self.locators["success_message"]):
                break

        # TODO implement message to telegram chat
