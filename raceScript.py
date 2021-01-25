# Jeff Wilson
# Race CTF Script

import socket

# Server Info
host = '127.0.0.1'
port = 19999
bufferSize = 2048

# Connect to the Server
r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect((host, port))

while True:
    d = r.recv(bufferSize).decode()
    print(d)

    # Decode the ASCII that was returned from the Server
    s = d.split("'")[-2]
    print(s)
    c = chr(int(s,2))
    print(c)
    r.send((c+'\n').encode())



