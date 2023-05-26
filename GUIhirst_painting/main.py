import colorgram
import turtle
import random
colors = colorgram.extract('image.jpg', 12)

#rgbList = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189)]
rgbList = []

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    rgbList.append((r, g, b))

timmy = turtle.Turtle()
timmy.color("black", "red")
turtle.colormode(255)


timmy.penup()
y = -256
timmy.setpos(-256, y)

for i in range(10):
    for j in range(10):
        timmy.pendown()
        timmy.dot(20,random.choice(rgbList))
        timmy.penup()
        timmy.forward(50)
    y += 50
    timmy.setposition(-256, y)



screen = turtle.Screen()
screen.exitonclick()