from turtle import *
class face:
    def __init__(self, x, y):
        self.size = (90)
        self.coord = (x , y)
        self.nosesize = "small"

    def setSize(self, radius):
        self.size = radius

    def draw(self):
        self.reset()
        pensize(3)
        speed(0)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye (45)
        self.drawnose()
        self.drawMouth()
        pensize(5)

    def reset(self):
        penup()
        goto(self.coord)
        setheading(0)

    def drawEye(self, turn):
        penup()
        left(turn)
        forward(self.size / 2)
        pendown()
        dot(self.size / 10)
        self.reset()

    def drawMouth(self):
        penup()
        right(135)
        forward(self.size/1.7)
        left(90)
        pendown()
        circle(self.size/1.7,90)
        self.reset()

    def drawnose(self):
        if self.nosesize == 'large' :
            dot(self.size/2, "grey")
        elif self.nosesize == 'small' :
            dot(self.size/6, "grey")
        else:
            dot(self.size/4, "grey")
            self.reset()

    def drawOutline(self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        circle(self.size)
        self.reset()
    


f1 = face(0 , 0)
f1.draw()
showturtle()
done()
