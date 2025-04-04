from turtle import Turtle, Screen
import random


PLAYER_POSITIONS = (-560,0)
OPPONENT_POSITIONS = (540,0)
MOVE_DISTANCE = 40
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle():
    def __init__(self):
        self.create_player()
        self.create_opponent()  
    
    def create_player(self):
        self.player = Turtle('square')
        self.player.speed('fastest')
        self.player.color("white")
        self.player.shapesize(1, 4)
        self.player.penup()   
        self.player.goto(PLAYER_POSITIONS)
        self.player.setheading(90)
    
    def create_opponent(self):
        self.opponent = Turtle('square')
        self.opponent.speed('fastest')
        self.opponent.color("white")
        self.opponent.shapesize(1, 4)
        self.opponent.penup()    
        self.opponent.goto(OPPONENT_POSITIONS)
        self.opponent.setheading(90)
    
        
    def player_up(self):
        self.player.seth(UP)
        self.player.forward(MOVE_DISTANCE)

    def player_down(self):
        self.player.seth(DOWN)
        self.player.forward(MOVE_DISTANCE)
            
    def opponent_up(self):
        self.opponent.seth(UP)
        self.opponent.forward(MOVE_DISTANCE)

    def opponent_down(self):
        self.opponent.seth(DOWN)
        self.opponent.forward(MOVE_DISTANCE)
