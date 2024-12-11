# pages/channel_groups_page.py
from config import SOURCE_DOMAIN
from pages.base_page import BasePage

class ChannelGroupsPage(BasePage):
    URL = f"https://{SOURCE_DOMAIN}/playlist/groups"

    locators = {
        'adults_chk': "input[value='10']",
        'armenian_chk': "input[value='11']",
        'ukrainian_chk': "input[value='12']",
        'usa_chk': "input[value='13']",
        'belorus_chk': "input[value='15']",
        'azer_chk': "input[value='16']",
        'kazakh_chk': "input[value='18']",
        'tochik_chk': "input[value='19']",
        'uzbek_chk': "input[value='20']",
        'moldova_chk': "input[value='21']",
        'turkish_chk': "input[value='22']",
        'greece_chk': "input[value='23']",
        'submit_btn': "button[type='submit']"
    }

    def __init__(self, sb):
        super().__init__(sb)

    def open_channel_groups_page(self):
        self.sb.open(self.URL)

    def config_playlist(self):
        self.open_channel_groups_page()
        for key, value in self.locators.items():
            self.sb.click(self.locators[key])
        self.sb.sleep(2)
