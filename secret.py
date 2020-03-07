


import itertools as its

def judgeRepeated(array):
    nums={}
    for i in array:
        if i  not in nums:
            nums[i]=i
        else:
            return False
    return True




#words="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
words = input("输入生成字符：")
pass_words = ""
dic = open("passwd.txt","w")
#passwd = its.product (pass_words,repeat=4)
#dic = open("passwd.txt","w")
m1 = input("最短长度：")
#print(type(m1))
m2 = input("最大长度：")
m3 = int(input("允许输出的密码个数："))
m4 = int(input("输出密码位数："))
m5 = input("停止字符：")
if m3 == 0:
    if m4 == 0:
        for x in range(int(m1),int(m2)+1):
            passwds = its.product(words,repeat=x)            
            for passwd in passwds:
                #print(type(passwd))
                if int(m5)==0:
                    #print(passwd)
                    if judgeRepeated(passwd):
                        dic.write("".join(passwd)+'\n')
                else:
                    dic.write("".join(passwd)+'\n') 
                    if "".join(passwd)==m5:
                        break

                    
       
    else:
         for x in range(int(m1),int(m2)+1):
            passwds = its.product(words,repeat=x)
            for passwd in passwds:
                 if len(passwd)==m4:
                    if int(m5)==0:
                        dic.write("".join(passwd)+'\n')
                    else:
                        dic.write("".join(passwd)+'\n') 
                        if "".join(passwd)==m5:
                            break
         

else :
    m3_1 = 0
    for x in range(int(m1),int(m2)+1):
        passwds = its.product(words,repeat=x)        
        for passwd in passwds:           
                if m4 == 0:          
                            if m3_1 < m3:
                                if int(m5)==0:
                                    dic.write("".join(passwd)+'\n')
                                    m3_1=m3_1+1
                                else:
                                    dic.write("".join(passwd)+'\n')
                                    m3_1=m3_1+1 
                                    if "".join(passwd)==m5:
                                        break            
                            
                else :
                            if len(passwd)==m4:
                                if m3_1 < m3:
                                    if int(m5)==0:
                                        dic.write("".join(passwd)+'\n')
                                        m3_1=m3_1+1
                                    else:
                                        dic.write("".join(passwd)+'\n')
                                        m3_1=m3_1+1 
                                        if "".join(passwd)==m5:
                                                break
                                    
                            else :
                                break
dic.close()
'''#指定开始字符读取
file1 = open('D:\大四下\老于的网络\\1\passwd.txt','r') 
file2 = file1.readlines()
#print(int(len(file2)/2))
m6 = input("指定开始输出字符：")
file3 = list(file2)
#print(file3)
print("从指定位置输出为：")
for p in range(0,len(file3)):
    #print(p)
    if file3[p]==m6+'\n':
        for q in range(p,len(file3)):
            if file3[q]!='\n':
                print(file3[q]+"  ")'''

