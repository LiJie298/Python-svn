# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import svn.local as local
import datetime

deployRevision = '0.5.0.6'
basePath = 'E:/heren/deployment/deploy-sourcecode/tags'
svnSavePath = 'E:/heren/deployment/svn'
pathPam = 7
jarPam = 8
sourcePathList = []
sourceJarPathList = []
isPath = ''

def getFileResource(basePath, thisVersion,isPath):
    if os.path.isdir(basePath):
        tempList = os.listdir(basePath)
        for i in tempList:
            temp = basePath + "/" + i
            if isPath != '' :
                if(temp.count("heren-core")>0):
                    if temp.count("/") < 7:
                        getFileResource(temp, thisVersion,isPath)
                    else:
                        if temp.count(thisVersion) > 0:
                            sourcePathList.append(temp)
                else :
                    if temp.count("/") < 8:
                     getFileResource(temp, thisVersion,isPath)
                    else:
                        if temp.count(thisVersion) > 0:
                            sourcePathList.append(temp)
            else:
                if temp.count("/") < 7:
                    getFileResource(temp, thisVersion,isPath)
                else:
                    if temp.count(thisVersion) > 0:
                        sourcePathList.append(temp)
    else:
        print "目录不正确,请核实你的路径+\n" + basePath


def getSvnVersion(sourcePathList, preVersion,isPath):
    sourceSvnDiffInfo = []
    for source in sourcePathList:
        if os.path.isdir(source):
            projectName = getProjectName(source)
            print  str(source)
            clicentInfo = local.LocalClient(str(source)).info()
            jj = local.LocalClient(source).log_default(revision_from=preVersion,
                                                       revision_to=clicentInfo.get('commit_revision'))
            infoTemp = ""
            for j in jj:
                if j.msg == None:
                    msg1 = ""
                else:
                    msg1 = j.msg
                infoTemp += str(j.revision) + '\t' + j.author + '\t' + msg1 + '\n'
            editSvnTxt(svnSavePath, projectName, infoTemp)


def editSvnTxt(svnSavePath, ProjectName, svnInfo):
    if not os.path.isdir(svnSavePath):
        os.makedirs(svnSavePath)
    else:
        testfile = svnSavePath + "/" + ProjectName + ".txt"
        if not os.path.exists(testfile):
            f = open(testfile, 'w')
        else:
            f = open(testfile, "a")
        f.write(str(svnInfo).encode("utf-8"))
        print testfile +"创建成功"
        f.close()


def getProjectName(source):
    baktem = "heren"
    if deployRevision == None or deployRevision == "":
        return
    else:
        tem = str(source).rsplit("/")
        if str(source).count("heren-core")>0:
            baktem = tem[len(tem)-2]
        else:
            baktem =tem[len(tem)-1]
    return baktem


try:
    svnSavePath = svnSavePath + "/" + deployRevision
    print "----------------保存地址为----------------\n" + svnSavePath
    isPath = 'patch1'
    getFileResource(basePath, deployRevision,isPath)
    for item in sourcePathList :
        print item
    getSvnVersion(sourcePathList, '39736',isPath)
    print "成功！！！"
except Exception, e:
    print "创建失败！！；原因是\n" + e.message;
finally:
    print "谢谢使用"

