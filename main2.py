import turtle
sc = turtle.Screen()
sc.bgcolor("orange")
sc.setup(400,400)
turtle.title("Welcome to Turtle Window")

#object of the turtle
t= turtle.Turtle()
# first triangle for star
t.forward(100) # draw base
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
# shifting turtles position
t.penup()
t.right(150)
t.forward(50)
t.pendown()
t.right(90)
# second triangle
t.forward(100) # draw base
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.penup()
t.forward(100)
t.pendown()
turtle.done()
