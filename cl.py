# -*- coding: utf-8 -*-
__author__ = 'jimshen'
import os
import re
import chardet

file = open("d:/1.txt","r")
fw= open("d:/res.txt","w")
for line in file:
    ot={}
    arr = line.strip().split(";")
    for a in arr:
        if re.compile(r"(.*N6\-\d+).*").match(a)<>None:
            ot[re.compile(r"(.*N6\-\d+).*").match(a).group(1)]=1
        if re.compile(ur'.*(敏行楼\d+).*'.encode('utf-8')).match(a)<>None:
            ot[re.compile(ur'.*(敏行楼\d+).*'.encode('utf-8')).match(a).group(1)]=1
    if not ot:
        print
    else:
        for key in ot:
            print key.decode('utf-8'),
        print
file.close()
fw.close()