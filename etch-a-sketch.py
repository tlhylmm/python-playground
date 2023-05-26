import turtle

timmy = turtle.Turtle()
timmy.speed(0)
screen = turtle.Screen()

def move_forward():
    timmy.forward(10)

def turn_right():
    timmy.right(5)

def turn_left():
    timmy.left(5)

def move_back():
    timmy.back(10)    

def create_turtle():
    terry = turtle.Turtle()

def clear():
    timmy.home()
    timmy.clear()
 
screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(turn_left, "a")
screen.onkeypress(move_back, "s")
screen.onkeypress(turn_right, "d")
screen.onkey(clear, "c")
















screen.exitonclick()