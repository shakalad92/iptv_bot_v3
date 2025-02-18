from twocaptcha import TwoCaptcha


class CaptchaSolver:
    def __init__(self, api_key: str, site_key: str, site_url: str):
        self.solver = TwoCaptcha(api_key)
        self.site_key = site_key
        self.site_url = site_url

    def solve_captcha(self):
        try:
            result: TwoCaptcha = self.solver.recaptcha(
                sitekey=self.site_key,
                url=self.site_url)
        except Exception as e:
            raise Exception
        else:
            return result['code']
