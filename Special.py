# -*- coding: utf-8 -*-
__author__ = 'jimshen'

import MySQLdb

from RoomCellItem import RoomCellItem

def load():
    f=open("d:/123/1.txt")
    for line in f:
        arr=line.split(",")
        item=RoomCellItem()
        item.weekDay=arr[3]
        item.frequency=u"周"
        item.classId=arr[2]
        item.courseName=arr[0]
        item.duration=2
        item.teacherName=arr[1]
        item.timePoint=arr[4]
        item.weeks=arr[5]
        item.room=arr[6].strip()
        yield item
    f.close()

def save2db():
        table_name = "s-2015-2016-2"
        try:
            conn =MySQLdb.connect(host="labs.cse.cslg.cn",user="root",passwd="password",db="syweb",charset="utf8")
            cur = conn.cursor()
            for item in load():
                item.expand()
                #item.printMe()
                for w in item.weeks:
                    sql="insert into `%s`(lab_name,course_name,teacher_name,class_id,time_point,duration,weekday,week,evaluation_form) values('%s','%s','%s','%s','%s',%s,%s,%s,'%s');" % (table_name,item.room,item.courseName,item.teacherName,item.classId,item.timePoint,item.duration,item.weekDay,w,item.evaluationForm)
                    print sql
                    #cur.execute(sql)
            # sql="update `%s` a,lab_room b set a.lab_name=b.room_id where a.lab_name=b.room_name" % table_name
            # cur.execute(sql)
            # conn.commit()
        except Exception,e:
            print e

if __name__=="__main__":
    save2db()