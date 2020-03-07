from PIL import ImageGrab  
import os
import socket
from EMAIL import fsend
import time


def can_do():
    app_dir = ('D:\百度网盘\BaiduNetdisk\\BaiduNetdisk.exe')
    os.startfile(app_dir)
    time.sleep(6)
    bbox = (0, 0, 1920, 1080)  
    im1 = ImageGrab.grab(bbox)  
    im1.save('D:\大四下\老于的网络\\4\\cut_screen.png')
    im2 = ImageGrab.grab(bbox)
    fsend("cut_screen.png")
    
    fd = open("port.txt","w")
    f = os.popen("netstat -an", "r")
    shuchu = f.read()
    fd.write(shuchu)
    fd.close
    f.close()
    time.sleep(10)
    fsend("port.txt")

#can_do()


