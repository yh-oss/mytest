import sys,socket
import getpass



def getipaddrs(hostname):
    result=socket.getaddrinfo(hostname,None,0,socket.SOCK_STREAM)
    return [x[4][0] for x in result]    
hostname=socket.gethostname()
Fully_qualified_name = socket.getfqdn(hostname)
user_name = getpass.getuser() # 获取当前用户名
IP_address =""
for x in range(0,len(getipaddrs(hostname))):
    IP_address = IP_address +"\n"+ ''.join(getipaddrs(hostname)[x])
print ("hostname is:"+hostname+'\n'+ "Fully_qualified name:"+socket.getfqdn(hostname)+'\n'+"当前用户名:"+user_name+'\n'+"IP address:"+IP_address)