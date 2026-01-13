import turtle
sc = turtle.Screen()
sc.bgcolor("orange")
sc.setup(400,400)
turtle.title("Welcome to Turtle Window")

#object of the turtle
t= turtle.Turtle()
for i in range(1,3):     # for loop executes 2 times
 t.forward(200)
 t.right(90)
 t.forward(100)
 t.right(90)
turtle.done()

