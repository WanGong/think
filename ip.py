import requests
from email.message import EmailMessage
import smtplib
import os


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


def getLastIp(path="/tmp/ip"):
    res = ""
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return res


def updateIp(cur_ip, path="/tmp/ip"):
    with open(path, "w") as f:
        f.write(cur_ip)


if __name__ == "__main__":
    sender = "xxxx@outlook.com"
    recipient = "xxx@qq.com"
    pwd = "xxx"

    cur_ip = getIp().text
    last_ip = getLastIp()

    if cur_ip != last_ip:
        print(f"cur ip: {cur_ip}, last ip: {last_ip}")
        send(cur_ip, sender, recipient, pwd)
        updateIp(cur_ip)
    else:
        print("ip not changed")
