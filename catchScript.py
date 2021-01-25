# Jeff Wilson
# Catch em ALL CTF Script

import base64

# Decode the Base 64 from .txt file gathered from Server
o = b''
with open("catchthemall.txt", "r") as f:
    count = 0
    for line in f:
        if(count) % 8 == 0:
            lineDecode = base64.b64decode(line)
            print(lineDecode)






