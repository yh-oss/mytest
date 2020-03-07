
import os
import sys
import win32com.client
import pywintypes
import threading
import pythoncom



#import Crypto

def docx(file):
    passwd_dir = "D:\大四下\老于的网络\\3\\3_1\\"
    #for x in ("0","100000","200000","300000","400000","500000","600000","700000","800000","900000","1000000","1100000","1200000","1300000","1400000","1500000","1600000","1700000","1800000"):
    print(file)
    passwd=[]
    dic = open(passwd_dir+"newfile"+file+".txt","r")
    data=dic.readline().strip('\n')
    while data:
        passwd.append(data)
        data=dic.readline().strip('\n')
    dic.close()
    pythoncom.CoInitialize()
    wps1=win32com.client.Dispatch('Kwps.application')
    wps1.Visible=1
    wps1.DisplayAlerts = 0
    for i in passwd:
        try:
            d=wps1.Documents.Open('D:\大四下\老于的网络\python msoffice\\下一步工作.docx',PasswordDocument=i)
        except :
            print(i)
            continue
        print("succcccceesss"+i)
        open("D:\大四下\老于的网络\\3\\"+'success_word'+str(i),'w')

def main():
    p1 = threading.Thread(target=docx,args=("700000",))
    p1.start()  
'''
    p2 = threading.Thread(target=docx,args=("100000",))
    p2.start()  

    p3 = threading.Thread(target=docx,args=("200000",))
    p3.start() 

    p4 = threading.Thread(target=docx,args=("300000",))
    p4.start()  

    p5 = threading.Thread(target=docx,args=("400000",))
    p5.start() 

    p6 = threading.Thread(target=docx,args=("500000",))
    p6.start()  

    p7 = threading.Thread(target=docx,args=("600000",))
    p7.start()  

    p8 = threading.Thread(target=docx,args=("700000",))
    p8.start() 

    p9 = threading.Thread(target=docx,args=("800000",))
    p9.start()  

    p10 = threading.Thread(target=docx,args=("900000",))
    p10.start() 

    p11 = threading.Thread(target=docx,args=("1000000",))
    p11.start() 

    p12 = threading.Thread(target=docx,args=("1100000",))
    p12.start()  

    p13 = threading.Thread(target=docx,args=("1200000",))
    p13.start()  

    p14 = threading.Thread(target=docx,args=("1300000",))
    p14.start() 

    p15 = threading.Thread(target=docx,args=("1400000",))
    p15.start()  

    p16 = threading.Thread(target=docx,args=("1500000",))
    p16.start()  

    p17 = threading.Thread(target=docx,args=("1600000",))
    p17.start()  

    p18 = threading.Thread(target=docx,args=("1700000",))
    p18.start()  

    p19 = threading.Thread(target=docx,args=("1800000",))
    p19.start() 
'''

if __name__ == '__main__':
    main()
            
        
        
    
    
