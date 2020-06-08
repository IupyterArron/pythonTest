import math
class Point:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def getz(self):
        return self.z


class dist_from:
    def __init__(self,p1,p2):
        self.x=p1.getx()-p2.getx()
        self.y=p1.gety()-p2.gety()
        self.z=p1.getz()-p2.getz()
        #用math.sqrt（）求平方根
        self.len= math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
    #定义得到直线长度的函数
    def dist_from(self):
        return self.len

