# -*- coding: utf-8 -*-
__author__ = 'jimshen'

import MySQLdb
import re

from ExcelReader import ExcelReader
from CellItem import CellItem

class KebiaoReader(ExcelReader):

    def __init__(self,excel_file,by_index=0):
        ExcelReader.__init__(self,excel_file)
        self.table = self.data.sheets()[by_index]

    def iterator(self):
        for rownum in range(3,8):
            for colnum in range(2,9):
                #print self.table.cell(rownum,colnum).value.strip()
                if len(self.table.cell(rownum,colnum).value.strip())>0:
                    cv=self.table.cell(rownum,colnum).value.split("\n ")
                    for s in cv:
                        #print s
                        if len(s.strip())<>0:
                            yield self.parse(s,colnum-1)

    def parse(self,item,weekday):
        kcobj=CellItem()
        kcobj.weekDay=weekday
        pattern=re.compile(ur"(.*)(考.*)◇(.*)节/(.*)\((.*)\)\[(.*)\]◇(.*)◇(.*)")
        matches = pattern.match(item.strip())
        if matches:
            kcobj.courseName=matches.group(1)
            kcobj.evaluationForm=matches.group(2)
            kcobj.duration=matches.group(3)
            kcobj.frequency=matches.group(4)
            kcobj.weeks=matches.group(5)
            kcobj.timePoint=matches.group(6)
            kcobj.classId = matches.group(7)
            kcobj.teacherName=matches.group(8)
        return kcobj

    def semester(self):
        return self.table.cell(1,7).value

    def semester_alias(self):
        matches = re.compile('(\d+\-\d+).*(\d).*').match(self.table.cell(1,7).value)
        return matches.group(1)+"-"+matches.group(2)

    def room(self):
        matches = re.compile(u'(.*)教室课程表').match(self.table.cell(0,0).value)
        return matches.group(1)

    def save2db(self):
        semester = self.semester_alias()
        lab_room = self.room()
        table_name = "s-" + semester
        # print semester,"/",lab_room,"/",table_name
        try:
            conn =MySQLdb.connect(host="127.0.0.1",user="root",passwd="password",db="syweb",charset="utf8")
            cur = conn.cursor()
            for item in self.iterator():
                item.printMe()
                item.expand()
                item.printMe()
                for w in item.weeks:
                    sql="insert into `%s`(lab_name,course_name,teacher_name,class_id,time_point,duration,weekday,week,evaluation_form) values('%s','%s','%s','%s','%s',%s,%s,%s,'%s')" % (table_name,lab_room,item.courseName,item.teacherName,item.classId,item.timePoint,item.duration,item.weekDay,w,item.evaluationForm)
                    print sql
                    cur.execute(sql)
            sql="update `%s` a,lab_room b set a.lab_name=b.room_id where a.lab_name=b.room_name" % table_name
            cur.execute(sql)
            conn.commit()
        except Exception,e:
            print e