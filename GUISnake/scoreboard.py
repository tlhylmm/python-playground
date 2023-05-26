from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = -1
        self.update()
        
    def update(self):
        self.clear()
        self.goto(x=0, y=310)
        self.score += 1
        self.write(arg=f"Score: {self.score}", align="Center", font=("Arial", 16, "normal"))

    def gameover(self):
        self.home()
        self.write(arg="Game Over :(", align="Center", font=("Arial", 24, "normal"))