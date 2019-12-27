'''
Created on 24-Dec-2019

@author: Abhishek Prajapati (ap07757(
'''
import os
import ntpath
from fileinput import filename

class FileUtils:

    '''
        Description: This method will return all the excel sheets present in the specified directory path.
        Author: Abhishek Prajapati
    '''
    def readAllExcels(self, dir):
        fileList = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".xlsx") or file.endswith(".xls"):
                    fileList.append(os.path.join(root, file))
        return fileList
    
    def path_leaf(self,path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
    
    def getFileNamesFromDir(self, dir):
        fileNameList = []
        fileList = FileUtils.readAllExcels(self, dir)
        for file in fileList:
            fileNameList.append(os.path.splitext(FileUtils.path_leaf(self, file))[0])
        return fileNameList
        
        