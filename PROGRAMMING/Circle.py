import math
class Circle:
    #construct a cicle object
    def __init__(self, radius = 1):

        self.radius = radius
    def getPerimeter(self):  # method
        return 2 *self.radius*math.pi
    def getArea(self):    #method
        return self.radius*math.pi*math.pi
    def setRadius(self, radius):
        self.radius = radius
