import os

# TELEGRAM VARIABLES
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# SERVICE PROVIDERS VARIABLES
SOURCE_DOMAIN = os.environ.get('SOURCE_DOMAIN')
PLAYER_DOMAIN = os.environ.get('PLAYER_DOMAIN')

# USERS VARIABLES
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
USER_PASSWORD = os.environ.get('USER_PASSWORD')
USER_EMAIL_PREFIX = os.environ.get('USER_EMAIL_PREFIX')

# EMAIL VARIABLES
GMAIL_ADMIN_ACCOUNT = os.environ.get('GMAIL_ADMIN_ACCOUNT')
GMAIL_ADMIN_PASSWORD = os.environ.get('GMAIL_ADMIN_PASSWORD')
GMAIL_SOURCE_PLAYER_ACCOUNT = os.environ.get('GMAIL_SOURCE_PLAYER_ACCOUNT')
GMAIL_SOURCE_PLAYER_PASSWORD = os.environ.get('GMAIL_SOURCE_PLAYER_PASSWORD')

# CAPTCHA VARIABLES
CAPTCHA_API_KEY = os.environ.get('CAPTCHA_API_KEY')
CAPTCHA_SITE_KEY = os.environ.get('CAPTCHA_SITE_KEY')
CAPTCHA_URL = os.environ.get('CAPTCHA_URL')

# JAVASCRIPT INTERCEPT
JS_INTERCEPT = '''
window.captchaParams = null;
const i = setInterval(() => {
    if (window.turnstile) {
        clearInterval(i);
        window.turnstile.render = (a,b) => {
            window.captchaParams = {
                websiteKey: b.sitekey,
                data: b.cData,
                pagedata: b.chlPageData,
                action: b.action,
                userAgent: navigator.userAgent
            };
            window.tsCallback = b.callback;
            return 'foo';
        };
    }
},10);
'''