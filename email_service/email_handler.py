import email
import imaplib
import re

from config import GMAIL_ADMIN_ACCOUNT, GMAIL_ADMIN_PASSWORD, SOURCE_DOMAIN, GMAIL_SOURCE_PLAYER_ACCOUNT, \
    GMAIL_SOURCE_PLAYER_PASSWORD, PLAYER_DOMAIN

SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

def get_transaction_verification_code() -> str:
    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login(GMAIL_ADMIN_ACCOUNT, GMAIL_ADMIN_PASSWORD)
    mail.select('inbox')
    _, msgnums = mail.search(None, f'(FROM "support@{SOURCE_DOMAIN}")')
    transaction_verification_code = []

    for msgnum in msgnums[0].split():
        _, data = mail.fetch(msgnum, "(RFC822)")

        message = email.message_from_bytes(data[0][1])
        for part in message.walk():
            if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                body = part.get_payload(decode=True).decode()
                transaction_verification_code.append(body)

    code = re.search("<li>код подтверждения - <b>(.*?)</b></li>", transaction_verification_code[-1])

    return code.group(0).split("<b>")[-1].split("</b>")[0]

def get_source_registration_verification_code() -> str:
    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login(GMAIL_SOURCE_PLAYER_ACCOUNT, GMAIL_SOURCE_PLAYER_PASSWORD)
    mail.select('inbox')
    _, msgnums = mail.search(None, f'(FROM "support@{SOURCE_DOMAIN}")')
    verification_code = []

    for msgnum in msgnums[0].split():
        _, data = mail.fetch(msgnum, "(RFC822)")

        message = email.message_from_bytes(data[0][1])
        for part in message.walk():
            if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                body = str(part.get_payload())
                code = re.search("<b>(.*?)</b>", body).group(0).split("<b>")[-1].split("</b>")[0]
                verification_code.append(code)

    return verification_code[-1]


def get_player_registration_activation_link():
    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login(GMAIL_SOURCE_PLAYER_ACCOUNT, GMAIL_SOURCE_PLAYER_PASSWORD)
    mail.select('inbox')
    _, msgnums = mail.search(None, f'(FROM "support@{PLAYER_DOMAIN}")')
    activation_links = []

    for msgnum in msgnums[0].split():
        _, data = mail.fetch(msgnum, "(RFC822)")

        message = email.message_from_bytes(data[0][1])
        for part in message.walk():
            if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                body = part.get_payload(decode=True).decode()
                activation_link = re.findall(r'href=[\'"]?([^\'" >]+)', body)[4]
                activation_links.append(activation_link)

    return activation_links[-1]
