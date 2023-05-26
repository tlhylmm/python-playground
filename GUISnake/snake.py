from turtle import Turtle
MOVE_DISTANCE = 21
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()            

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new = Turtle("square")
        new.penup()
        new.color("brown", "white")
        new.goto(position)
        self.snake.append(new)

    def extend(self):
        # add new segment to the same position as the last segment. it will
        # appear and start following the tail as long as the last segment moves
        self.add_segment(self.snake[-1].position())

    def move(self):
        """if ((self.snake[0].xcor() > 272 or self.snake[0].xcor() < -272)
            or (self.snake[0].ycor() > 272 or self.snake[0].ycor() < -272)):
            print("gameover")
            return  
        else:"""
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].xcor(), self.snake[i - 1].ycor())
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
        
    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)        

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)        
    
    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
        