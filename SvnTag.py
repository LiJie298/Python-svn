# -*- coding: utf-8 -*-
import commands
import os
import subprocess
import svn.local as local

codeBasePath = 'E:\\heren\\deployment\\deploy-sourcecode\\trunk'
tagsBasePath = 'E:\\heren\\deployment\\deploy-sourcecode\\tags'
svnServePath = 'https://192.168.1.78/svn/sourcecode/'
releaseVersion = '0.5.0.7'
patch = ''


def updateCode():
    if os.path.isdir(codeBasePath):
        # print os.getcwd()  获取当前工作目录
        os.chdir(codeBasePath)  # 切换到制定工作目录
        print os.getcwd()
        print "updating code..........."
        return os.popen("svn up")


def tagsProject(codeBasePath):
    tagsPath = ""
    sourceList = os.listdir(codeBasePath)
    for so in sourceList:
        temp = codeBasePath + "\\" + so
        if so == 'heren-his':
            tagsPath = tagsBasePath + '\\heren-his\\' + releaseVersion
            command = 'svn copy ' + temp + ' ' + tagsPath
            if os.popen(command):
                print 'copy code ...'
                os.system('svn add ' + tagsPath)
                os.popen('svn commit -m ' + "'打 '" + releaseVersion + "' tag ' ")
                print 'heren-his tag successfully'
            break
        else:
            if temp.count("\\") < 6:
                tagsProject(temp)
            else:
                if temp.count("message") > 0 or temp.count("report-project") > 0 or temp.count("heren-schedule") > 0:
                    jj = temp.rsplit('\\')
                    name = jj[len(jj) - 1]
                    os.chdir(temp)
                    tagsPath = tagsBasePath + '\\heren-core\\' + name + '\\' + releaseVersion
                    command = 'svn copy ' + temp + ' ' + tagsPath
                    os.system(command)
                    if os.popen('svn add ' + tagsPath):
                        os.system('svn commit -m ' + "'打 '" + releaseVersion + "' tag ' ")
                    print name + ' copy and tag successfully! \n'


def isExist(dirPath):
    if os.path.isdir(dirPath):
        os.remove(dirPath)


try:
    if not patch == '':
        releaseVersion += '\\' + patch
    if updateCode():
        print "update successfully"
        os.chdir(tagsBasePath)
        if os.popen('svn cleanup'):
            tagsProject(codeBasePath)
except Exception, e:
    print "error:" + e.message
