# coding=utf-8
import PyPDF4
import sys

pdfReader = PyPDF4.PdfFileReader(open('D:\大四下\老于的网络\python msoffice\\文档2.pdf','rb'))
if pdfReader.isEncrypted:
    print('try')
    File = open('D:\大四下\老于的网络\\3\\3_1\\newfile0')
    sfile = File.read()
    dic = sfile.split('\n')
    num = len(dic)
    for i in range(num):
        print('try '+str(i) +' ...')
        if pdfReader.decrypt(dic[i]):
            print(dic[i])
            #print('PDF有 '+ str(pdfReader.numPages) + '...')
            #print('内容摘要')
            pageObj = pdfReader.getPage(0)
            print(pageObj.extractText())
            break
        temp = dic[i].lower()
        if pdfReader.decrypt(temp):
            print(temp)
            #print('破解成功，密码是 ' + temp + '...')
            #print('PDF有 '+ str(pdfReader.numPages) + '...')
            #print('内容摘要')
            pageObj = pdfReader.getPage(0)
            print(pageObj.extractText())
            break
        print('失败')
    print('程序关闭...')
    sys.exit()

