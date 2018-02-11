#! python3

from bs4 import BeautifulSoup
import requests
import smtplib
import configparser


'''
Sender Username/Password and Recipient are extracted from c:\config.ini file. File should be formatted as follows:
[checkIP]
sender = user@gmail.com
pw = P@ssw0rd!
recipient = me@me.com
'''

config = configparser.ConfigParser()
config.read("c:\config.ini")
sender = config.get("checkIP", "sender")
pw = config.get("checkIP", "pw")
recipient = config.get("checkIP", "recipient")


def last_ip():
    with open("ip.txt") as i:
        last_ip = i.read()
        print("Last IP: {0}".format(last_ip))
        return last_ip


def current_ip():
    ipvoid = requests.get('http://www.ipvoid.com/')
    soup = BeautifulSoup(ipvoid.text, "html.parser")
    inputs = soup.find_all('input')
    current = (inputs[9]['value'])
    print("Current IP: {0}".format(current))
    return current


def notify(ip):
    smtpObj = smtplib.SMTP('smtp.gmail.com:587')
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender, pw)
    smtpObj.sendmail(sender, recipient, 'Subject: IP: %s' % ip)
    smtpObj.quit()
    print("Notification sent to {0}".format(recipient))


def update(ip):
    with open("ip.txt", "w") as i:
        i.write(ip)


def main():
    lastIP = last_ip()
    newIP = current_ip()
    if lastIP != newIP:
        notify(newIP)
        update(newIP)
    else:
        print("IP has not changed")


if __name__ == "__main__":
    main()



