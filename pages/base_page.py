from config import SOURCE_DOMAIN
class BasePage:
    def __init__(self, driver):
        self.sb = driver

    def logout_source(self):
        self.sb.get(f"https://{SOURCE_DOMAIN}/auth/signout")
