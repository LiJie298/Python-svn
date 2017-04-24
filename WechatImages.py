# -*- coding: utf-8 -*-
import itchat
import math
import PIL.Image as Image
import os
from __future__ import print_function

saveBasePath = 'E:/images' + "/"
itchat.auto_login(True)
chatroomsList = []
friends = []


def saveFriendPhoto(type, fileName, friends):
    groupList = {}
    sPath = saveBasePath + fileName + "/" + type
    if type == "group":
        for i in friends:
            # pathname = sPath + '/' + i['NickName'].encode('utf-8')
            pathname = sPath + '/' + i['NickName']
            groupList.setdefault(pathname, i['MemberList'])
    else:
        groupList.setdefault('self', friends)
    for key, value in groupList.items():
        # key = key.decode('utf-8').encode('gbk')
        if not os.path.isdir(key):
            os.mkdir(key)

        print ("created new  file")
        num = 0
        for ii in value:
            img = itchat.get_head_img(userName=ii["UserName"])
            fileImage = open(key + "/" + str(num) + ".jpg", 'wb')
            try:
                fileImage.write(img)
            except TypeError, Error:
                print (Error.message)
            finally:
                fileImage.close()
            num += 1
            # editImage(key)


def editImage(sourcePath):
    ls = os.listdir(sourcePath)
    each_size = int(math.sqrt(float(640 * 640) / len(ls)))
    lines = int(640 / each_size)
    image = Image.new('RGBA', (640, 640))
    x = 0
    y = 0
    for i in range(0, len(ls) + 1):
        try:
            img = Image.open(sourcePath + '/' + str(i) + ".jpg")
        except IOError, e:
            print("Error : " + e)
        else:
            img = img.resize((each_size, each_size), Image.ANTIALIAS)
            image.paste(img, (x * each_size, y * each_size))
            x += 1
            if x == lines:
                x = 0
                y += 1

    for yy in range(20, -20, -2):
        for xx in range(-30, 30, 1):
            y = yy / 10
            x = xx / 10
            if (x * x + y * y - 1) * (x * x + y * y - 1) * (x * x + y * y - 1) <= x * x * y * y * y:
                print("lijie", end='')
            else:
                print("", end='')
            print()

    try:
        image.save(sourcePath + "/all.jpg")
    except IOError, e:
        print("save error！" + str(e.message))
    except Exception, e:
        print("send error！" + str(e.message))


def getChatroomsFrient(itchat, chatRoomName):
    tempList = []
    chatroomsList = []
    if chatRoomName is None:
        chatroomsList = itchat.get_chatrooms()
    else:
        chatroomsList = itchat.search_chatrooms(name=chatRoomName.decode('utf-8'))
        for item in chatroomsList:
            itchat.update_chatroom(item["UserName"])
            item = itchat.update_chatroom(item["UserName"])
            tempList.append(item)
    return tempList


def main():
    friends = getChatroomsFrient(itchat, '今晚月色很美')
    saveFriendPhoto("group", "test1", friends)

    # friends = itchat.get_friends(update=True)[0:]
    # saveFriendPhoto("your", "test", friends)


main()
