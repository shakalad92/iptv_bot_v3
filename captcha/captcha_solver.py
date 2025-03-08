import time
import requests
from twocaptcha import TwoCaptcha
from config import CAPTCHA_API_KEY


class CaptchaSolver:
    def __init__(self):
        self.api_key = CAPTCHA_API_KEY  # Сохраняем ключ вручную
        self.solver = TwoCaptcha(self.api_key)

    def solve_google_captcha(self, site_key: str, site_url: str):
        try:
            result = self.solver.recaptcha(
                sitekey=site_key,
                url=site_url
            )
            return result['code']
        except Exception as e:
            raise Exception(f"Ошибка решения Google reCAPTCHA: {e}")

    def solve_turnstile_captcha(self, site_url: str, captcha_params: dict):
        task_payload = {
            "clientKey": self.api_key,  # Теперь используем сохраненный ключ
            "task": {
                "type": "TurnstileTaskProxyless",
                "websiteURL": site_url,
                "websiteKey": captcha_params["websiteKey"],
                "action": captcha_params["action"],
                "data": captcha_params["data"],
                "pagedata": captcha_params.get("pagedata")
            }
        }

        response = requests.post("https://api.2captcha.com/createTask", json=task_payload).json()

        if response.get("errorId", 1) != 0:
            raise Exception(f"Ошибка создания задачи: {response}")

        task_id = response["taskId"]

        for _ in range(30):
            time.sleep(5)
            result = requests.post(
                "https://api.2captcha.com/getTaskResult",
                json={"clientKey": self.api_key, "taskId": task_id}
            ).json()

            if result["status"] == "ready":
                return result["solution"]["token"]

        raise Exception("Cloudflare капча не решена.")