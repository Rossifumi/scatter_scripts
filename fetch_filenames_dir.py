# -*- coding: utf-8 -*-

import os

def readDir(dirPath):
    if dirPath[-1] == '/':
        print u'Remove / at the end of your file path'
        return
    allFiles = []
    if os.path.isdir(dirPath):
        fileList = os.listdir(dirPath)
        for f in fileList:
            f = dirPath+'/'+f
            if os.path.isdir(f):
                subFiles = readDir(f)
                allFiles = subFiles + allFiles #合并当前目录与子目录的所有文件路径
            else:
                allFiles.append(f)
        return allFiles
    else:
        return 'Error,not a dir'
 
if __name__ == "__main__":
    filePath = '/storage/jjxu/Pumch_vcf_stats/export_txt' #'D:\java\\answer\\Thinking in Java4 Answer' # refer root dir
    myFileNames = readDir(filePath)
    myFileNames.sort(cmp=None, key=None, reverse=False)
    file_output = open('filenames_list.txt','w')
    file_output.write("\n".join(myFileNames))
    file_output.close()