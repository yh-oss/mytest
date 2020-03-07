#-*- coding: UTF-8 -*-
import msoffcrypto
import sys

def foff():
	file = msoffcrypto.OfficeFile(open("D:\大四下\老于的网络\python msoffice\\网络攻防实践.xlsx", "rb"))
#list = ["123456","134498","4654165","12345678"]
# password = "12345678"
	passFile=open('D:\大四下\老于的网络\\3\\3_1\\newfile0.txt',encoding="utf-8")
	zpw=passFile.readlines()
	for line in zpw:
		get_progress=int((zpw.index(line)+1)*(50/len(zpw)))  #显示多少>
		get_pro=int(50-get_progress)#显示多少-
		percent=(zpw.index(line)+1)*(100/len(zpw))
		print("\r"+"["+">"*get_progress+"-"*get_pro+']'+"%.2f" % percent + "%",end="")
		password = line.strip('\n')
		try:
			file.load_key(password)
			file.decrypt(open("python msoffice/网络攻防实践1.xlsx", "wb"))
			print(password)
			sys.exit()
		except Exception :
		# print(0)
			pass

#off()