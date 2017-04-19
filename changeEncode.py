# -*- coding: utf-8 -*-
# Filename:changeEncode.py
import os

savePath = "E:\heren\dbChanaged"
sourcePath = "E:\heren\db"


def ChangeEncode(file, fromEncode, toEncode):
    try:
        sourceFile = os.path.join(sourcePath, file)
        f = open(sourceFile)
        s = f.read()
        f.close()
        u = s.decode(fromEncode)
        s = u.encode(toEncode)
        saveFile = os.path.join(savePath, file)
        f = open(saveFile, "w")
        f.write(s)
        return 0
    except Exception, e:
        print "发生错误：" + str(e)
        return -1
    finally:
        f.close()


def Do(dirname, fromEncode, toEncode):
    for root, dirs, files in os.walk(dirname):
        for _file in files:
            if (ChangeEncode(_file, fromEncode, toEncode) != 0):
                print "[转换失败:]" + _file
            else:
                print "[成功：]" + _file


def CheckParam(dirname, fromEncode, toEncode):
    encode = ["UTF-8", "GBK", "gbk", "utf-8", "gb18030", "gb2312"]
    if (not fromEncode in encode or not toEncode in encode):
        return 2
    if (fromEncode == toEncode):
        return 3
    if (not os.path.isdir(dirname)):
        return 1
    return 0


if __name__ == "__main__":
    error = {1: "第一个参数不是一个有效的文件夹", 3: "源编码和目标编码相同", 2: "您要转化的编码不再范围之内：UTF-8，GBK"}
    dirname = sourcePath
    fromEncode = "UTF-8"
    toEncode = "gbk"
    ret = CheckParam(dirname, fromEncode, toEncode)
    if (ret != 0):
        print error[ret]
    else:
        Do(dirname, fromEncode, toEncode)
