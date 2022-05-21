import turtle
tpg = turtle.Turtle()
tpg.shape("turtle")

n = int(input("How many sides do you want?"))
l = int(input("How long do you want?"))

for i in range(n):
    tpg.forward(l)
    tpg.right(360 / n)
