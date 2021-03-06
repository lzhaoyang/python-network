#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: login.py
@time: 2018/12/5
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import sys, smtplib, socket
from getpass import getpass

message_template = """To: {}
From: {}
Subject: Test Message from simple.py
Hello,
This is a test message sent to you from the login.py program
in Foundations of Python Network Programming.
"""


def main():
    if len(sys.argv) < 4:
        name = sys.argv[0]
        print("Syntax: {} server fromaddr toaddr [toaddr...]".format(name))
        sys.exit(2)

    server, fromaddr, toaddrs = sys.argv[1], sys.argv[2], sys.argv[3:]
    message = message_template.format(', '.join(toaddrs), fromaddr)

    username = input("Enter username: ")
    password = getpass("Enter password: ")

    try:
        connection = smtplib.SMTP(server)
        try:
            connection.login(username, password)
        except smtplib.SMTPException as e:
            print("Authentication failed:", e)
            sys.exit(1)
        connection.sendmail(fromaddr, toaddrs, message)
    except (socket.gaierror, socket.error, socket.herror,
            smtplib.SMTPException) as e:
        print("Your message may not have been sent!")
        print(e)
        sys.exit(1)
    else:
        s = '' if len(toaddrs) == 1 else 's'
        print("Message sent to {} recipient{}".format(len(toaddrs), s))
        connection.quit()


if __name__ == '__main__':
    main()
