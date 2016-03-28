__author__ = 'jimshen'

from CellItem import CellItem

class RoomCellItem(CellItem):
    room=""

    def printMe(self):
        print self.room ,
        super(RoomCellItem,self).printMe()