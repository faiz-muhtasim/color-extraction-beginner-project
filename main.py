from turtle import Turtle, Screen
import random
colors = ["red", "black", "green", "blue", "magenta", "pink", "yellow", "brown", "orange"]
tim = Turtle()
n = 0


def ol():
    for i in range(10):
        tim.penup()
        tim.hideturtle()
        tim.speed("fastest")
        tim.dot(15, colors[random.randint(0, 7)])
        tim.forward(30)


for i in range(10):
    ol()
    n += 30
    tim.setx(0)
    tim.sety(n)


screen = Screen()
screen.exitonclick()