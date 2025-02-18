class Rectangle:
    def __init__(self, width = 1, length =1 ):

        self.width = width
        self.length = length

    def getPerimeter(self):  # method
        return 2*(self.width + self.length)
    def getArea(self):    #method
        return self.width*self.length
    def setWidth(self, width):
        self.width = width
    def setlength(self, length):
        self.length = length

