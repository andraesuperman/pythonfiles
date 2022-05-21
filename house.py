import turtle # telling python that you will use turtle

t = turtle.Pen() # telling python to start using turtle

# for background
screen = turtle.Screen()
screen.bgcolor("gray")

# color and speed of turtle
# creating the house
t.color("black") # color of the turtle
t.shape("turtle") # classic, arrow, turtle, circle, square, triangle
t.speed(0)
 # fastest - 0
 # fast - 10
 # normal - 6
 # slow - 3
 # slowest - 1

# for creating base of the house (rectangle)
t.fillcolor('cyan')
t.begin_fill()
t.right(90)
t.forward(250)
t.left(90)
t.forward(400)
t.left(90)
t.forward(250)
t.left(90)
t.forward(400)
t.right(90)
t.end_fill()

# for top of the house (roof)
t.fillcolor('brown')
t.begin_fill()
t.right(45)
t.forward(200)
t.right(90)
t.forward(200)
t.left(180)
t.forward(200)
t.right(135)
t.forward(259)
t.right(90)
t.forward(142)
t.end_fill()

# for door and windows
t.right(90)
t.forward(400)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(75)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)
t.right(90)
t.forward(75)
t.left(90)
t.forward(15)
t.left(90)
t.forward(200)
t.right(90)
t.forward(15)
t.right(90)
t.forward(75)


turtle.done()
