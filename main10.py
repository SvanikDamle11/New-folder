from turtle import *
class face:
    def __init__(self, x, y):
        self.size = (90)
        self.coord = (x , y)

    def setSize(self, radius):
        self.size = radius 

    def reset(self):
        penup()
        goto(self.coord)

    def draw(self, reset):
        self.reset()
        pensize(3)
        speed(0)

    def draw(self):
        self.reset()
        pensize(3)
        speed(0)
        self.drawOutline()

    def draw(self):
        self.reset()
        pensize(3)
        speed(0)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye (45)
        self.drawlose()
        self.drawMouth()
        pensize(5)
    


f1 = face(0 , 0)
