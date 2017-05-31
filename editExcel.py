import xlrd
import xlwt
import os


def editExcel(filePath):
    if os.path.isdir(filePath):
        fileNameList = os.listdir(filePath)
        for fileName in fileNameList :
            fPath = filePath+'/'+fileName
