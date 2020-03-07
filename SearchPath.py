import os,zipfile


def fSearchPath(path):
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
    for folder,subFolders,files in os.walk(path):
        for file in files:#文件分析
            #AnalyzeFile(folder,file)
            if file.endswith('.txt') :
                result_txt.append(folder+"\\"+file)
            if file.endswith('.doc') :
                result_doc.append(folder+"\\"+file)
            if file.endswith('.docx') :
                result_docx.append(folder+"\\"+file)
            if file.endswith('.pdf') :
                result_pdf.append(folder+"\\"+file)
            if file.endswith('.zip') :
                result_zip.append(folder+"\\"+file)
            if file.endswith('.rar') :
                result_rar.append(folder+"\\"+file)
            if file.endswith('.jpg') :
                result_jpg.append(folder+"\\"+file)
            if file.endswith('.gif') :
                result_gif.append(folder+"\\"+file)
            if file.endswith('.png') :
                result_png.append(folder+"\\"+file)
            if file.endswith('.bmp') :
                result_bmp.append(folder+"\\"+file)
            if file.endswith('.mp4') :
                result_mp4.append(folder+"\\"+file)
            if file.endswith('.mp3') :
                result_mp3.append(folder+"\\"+file)
        for subFolder in subFolders:#递归遍历
            fSearchPath(subFolder)     


