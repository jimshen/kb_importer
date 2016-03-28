__author__ = 'jimshen'

import os
from KebiaoReader import KebiaoReader

kb_dir="d:/123"

if __name__=="__main__":
    for f in os.listdir(kb_dir):
        fname = kb_dir + os.sep + f
        print "processing ",f
        data = KebiaoReader(fname)
        data.save2db()