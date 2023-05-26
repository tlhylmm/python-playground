from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")
timmy.color("black", "red")
timmy.pensize(1)
timmy.speed(0)

colorchart = ["aquamarine", "blue", "brown1", "BlueViolet", "DarkGoldenRod1",
              "ForestGreen", "OrangeRed", "yellow", "red"]
angles = [0, 90, 180, 270]

for i in range(180):
    timmy.pencolor(random.choice(colorchart))
    timmy.circle(100)
    timmy.right(2)

screen = Screen()
screen.exitonclick()


