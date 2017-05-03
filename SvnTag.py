# -*- coding: utf-8 -*-
import os
import subprocess
import svn.local as local

codeBasePath = 'E:\\heren\\deployment\\deploy-sourcecode\\trunk'
tagsBasePath = 'E:\\heren\\deployment\\deploy-sourcecode\\tags'
svnServePath = 'https://192.168.1.78/svn/sourcecode/'
releaseVersion = '0.5.0.7'
patch = 'patch1'
def updateCode():
    if os.path.isdir(codeBasePath):
        # print os.getcwd()  获取当前工作目录
        os.chdir(codeBasePath)#切换到制定工作目录
        os.system("cd ")
        return os.popen("svn up")
def tagsProject(codeBasePath):
    sourceList = os.listdir(codeBasePath)
    for so in sourceList:
        temp = codeBasePath + "\\" + so
        if so == 'heren-his':
            command = 'svn copy ' + temp + ' ' + tagsBasePath + '\\heren-his\\' + releaseVersion
            if os.popen(command):
                os.system('add '+tagsBasePath + '\\heren-his\\' + releaseVersion)
                os.popen('svn commit -m '+"'打 '"+releaseVersion+"' tag ' "+ tagsBasePath + '\\heren-his\\' + releaseVersion)
                print 'tag successfully'
            break
        else:
            if temp.count("\\")<6:
                tagsProject(temp)
            else:
                if temp.count("message")>0 or temp.count("report-project")>0 or temp.count("heren-schedule")>0 :
                    jj = temp.rsplit('\\')
                    name = jj[len(jj)-1]
                    os.chdir(temp)
                    command = 'svn copy '+temp+' '+tagsBasePath+'\\heren-core\\'+name+'\\'+releaseVersion
                    os.system(command)
                    if os.popen('svn add '+tagsBasePath+'\\heren-core\\'+name+'\\'+releaseVersion):
                        os.system('svn commit -m '+"'打 '"+releaseVersion+"' tag ' "+ tagsBasePath + '\\heren-core\\'+name+'\\'+releaseVersion)
                    print name +' copy and tag successfully! \n'

def isExist (dirPath):
    if os.path.isdir(dirPath):
       os.remove(dirPath)


try:
    if not patch == '':
        releaseVersion += '\\'+patch
    updateCode()
    os.chdir(tagsBasePath)
    if os.popen('svn cleanup'):
        tagsProject(codeBasePath)
except Exception,e:
    print e.message
