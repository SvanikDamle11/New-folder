class rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w


    def area(self):
        print("Area of a rectangle is:", self.length * self.width)


obj = rectangle(10,14)
obj.area()



