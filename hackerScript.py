# -*- coding: utf-8 -*-
import base64, socket

host = '127.0.0.1'
port = 11111

r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect((host,port))

for x in range(10002):
    d = r.recv(2048).decode()
    if '==' in d:
        s = base64.b64decode(d).decode()
        print(x+1, " problem(s) decoded! \n")
        r.send((s + '\n').encode())
    else:
        print(d)
        # print("Hit Something! \n")

