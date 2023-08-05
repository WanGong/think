import requests
from email.message import EmailMessage
import smtplib


def getIp():
    return requests.get("https://ipinfo.io/ip")


def send(msg, sender, recipient, pwd):
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = "IP notify"
    email.set_content(msg)

    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(sender, pwd)
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()


if __name__ == "__main__":
    sender = "xxx@outlook.com"
    recipient = "xxx@qq.com"
    pwd = "xxx"

    response = getIp()
    msg = f"code: {response.status_code}, ip: {response.text}"
    send(msg, sender, recipient, pwd)
