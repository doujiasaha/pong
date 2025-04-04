from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1.25, 1.25)
        self.penup()
        self.speed("fastest")
        self.goto(0,0)
        self.rand_pos()

    # Set Coordinate to either bottom-left, bottom-right, top-left or top-right from 0,0
    def move(self):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)

    # Set angle for ball
    def rand_pos(self):
        self.x_move = 2.5* random.randrange(-1,2,2)
        self.y_move = 2.5* random.randrange(-1,2,2)

    #when top/bottom wall is hit, reverse Y-axis
    def wall_bounce(self):
        self.y_move *= -1

    #when paddle is hit, reverse X-axis
    def paddle_bounce(self):
        self.x_move *= -1


    #reset to 0,0
    def reset(self):
        self.goto(0, 0)
        self.rand_pos()