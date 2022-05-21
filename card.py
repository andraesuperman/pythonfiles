import turtle
import time
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(800, 600)
wn.title("Deck of Cards Simulator")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

#THE  CLASS
class Card():
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.symbols = {"D":"♦️", "C":"♣️", "H":"♥️", "S":"♠️"}
    def print_card(self):
        print(f"{self.name}{self.symbols[self.suit]}")

    def render(self, x, y, pen):
        # Draw border
        pen.penup()
        pen.goto(x, y)
        pen.color("blue")
        pen.goto(x-50, y+75)
        pen.begin_fill()
        pen.pendown()
        pen.goto(x+50, y+75)
        pen.goto(x+50, y-75)
        pen.goto(x-50, y-75)
        pen.goto(x-50, y+75)
        pen.end_fill()
        pen.penup()
        if self.name != "":
            # Draw suit in the middle
            pen.color("white")
            pen.goto(x-18, y-30)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))

            # Draw top left
            pen.goto(x-40, y+45)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x-40, y+25)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))

            # Draw bottom right
            pen.goto(x+30, y-60)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x+30, y-80)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
card1 = Card("10" , "C")
card1.render(0,0,pen)
wn.mainloop()
