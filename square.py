import turtle
tpg = turtle.Turtle()
tpg.shape("turtle")
tpg.speed(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
tpg.getscreen().bgcolor("yellow")
tpg.fillcolor("green")
tpg.begin_fill()

for i in range(100):
    tpg.circle(5*i)
    tpg.circle(-5*i)
    tpg.left(i)

tpg.end_fill()

turtle.done()
