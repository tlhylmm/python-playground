from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=685, height=685)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

#draw the frame:
frame = Turtle()
frame.hideturtle()
frame.color("white")
frame.pensize(5)
frame.penup()
frame.goto(x = -308, y = -308)
frame.pendown()
frame.goto(x = -308, y = +308)
frame.goto(x = +308, y = +308)
frame.goto(x = +308, y = -308)
frame.goto(x = -308, y = -308)

thomas = Snake()
food = Food()
scoreboard = Scoreboard()

#movements
screen.listen()
screen.onkey(thomas.up, "Up")
screen.onkey(thomas.down, "Down")
screen.onkey(thomas.left, "Left")
screen.onkey(thomas.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.075) 
    thomas.move()

    #detect if snake reached the food
    if thomas.snake[0].distance(food) < 15:
        food.teleport()
        scoreboard.update()
        thomas.extend()

    #detect if it hits the wall
    if (thomas.snake[0].xcor() > 284 or thomas.snake[0].xcor() < -284
        or thomas.snake[0].ycor() > 284 or thomas.snake[0].ycor() < -284):
        game_is_on = False
        scoreboard.gameover()
        screen.update()
        input()

    #detect if it collides with its own tail
    for segment in thomas.snake:
        # pass the head since it can't collide with itself
        if segment == thomas.snake[0]:
            pass
        elif thomas.snake[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()
            input()