#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: search5.py
@time: 2018/10/7 12:59
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import socket
from urllib.parse import quote_plus

request_text = """\
GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1 \r\n
Host: maps.google.com:80\r\n
User-Aget: search4.py (Foundations of Python Network Programing)\r\n
Connection:close\r\n
\r\n
"""
target_address = "207 N.Defiance St,Archbold, OH"


# 问题：底层的socket如何使用代理
# 调用api依然是需要google 的key的
def geocode(address):
    sock = socket.socket()
    sock.connect(('10.8.0.153', 1081))
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply = b""
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8'))

    # 需要自己按照http的规范去解析返回过来的数据，然后封装成各个部分
    # json_data = json.loads(raw_reply.decode('utf-8'))
    # print(json_data)


if __name__ == '__main__':
    geocode(target_address)
