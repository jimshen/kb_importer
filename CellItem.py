# -*- coding: utf-8 -*-
__author__ = 'jimshen'

class CellItem(object):
    #星期几？
    weekDay=""
    #课程名称
    courseName=""
    #考核形式
    evaluationForm=""
    #每次节数
    duration=""
    #上课频率，每周，单周或双周
    frequency=""
    #上课周次
    weeks=""
    #上课时段，如1-2,3-4,5-6等
    timePoint=""
    #班号
    classId=""
    #任课教师姓名
    teacherName=""

    def expand(self):
        y=[]
        weeks_array = self.weeks.split(",")
        for week in weeks_array:
            wk=week.split("-")
            bg=int(wk[0][1] if wk[0].startswith("0") else wk[0])
            ed=int(wk[1][1] if wk[1].startswith("0") else wk[1])
            y.extend([x for x in range(bg,ed+1)])
        self.weeks=[]
        if self.frequency==u"双周":
            for i in y:
                if i%2==0:
                    self.weeks.append(i)
        if self.frequency==u"单周":
            for i in y:
                if i%2==1:
                    self.weeks.append(i)
        if self.frequency==u"周":
            self.weeks=y

    def printMe(self):
        print self.weekDay,"|",self.courseName,"|",self.evaluationForm,"|",self.duration,"|",self.frequency,"|",self.weeks,"|",self.timePoint,"|",self.classId,"|",self.teacherName