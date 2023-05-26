from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.goto(x=random.randint(-285, 285), y=random.randint(-285, 285))
        self.teleport()

    def teleport(self):
        self.goto(x=random.randint(-285, 285), y=random.randint(-285, 285))
