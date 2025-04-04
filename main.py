"""
screen for board
screen black

2 scoreboards
1 for player 
1 for opponent

2 'boards' -> could be 1x3 turtle as in snake element.
movement only up and down

ball object -> could use food from snake for that
# need to figure out trajectory
-> collision for wall 
-> collision for paddle

update score when ball goes through
respawn ball at some point from middle
---------------
"""

from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time, random, subprocess

RIGHT_WALL = -600
LEFT_WALL = 600
TOP_WALL = 300
BOTTOM_WALL = -300


# added subprocess to use a collision soundeffect. apparently pygame is broken on 3.13 + macOS
def play_sound():
    subprocess.Popen(["afplay", "collision.wav"]) 

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=600)
screen.title("Pong Game!")
screen.tracer(0)

player = Paddle()
scoreboard = Scoreboard()
ball = Ball()


screen.listen()
screen.onkey(player.player_up, "w")
screen.onkey(player.player_down, "s")
screen.onkey(player.opponent_up, "Up")
screen.onkey(player.opponent_down, "Down") 

# print(player.player.pos())
# print(player.opponent.pos())

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.016)
    ball.move()

    if ball.ycor() > TOP_WALL or ball.ycor() < BOTTOM_WALL:
        play_sound()
        ball.wall_bounce()
        
    if -580 < ball.xcor() < -540 and ball.distance(player.player) < 30:
        play_sound()
        ball.paddle_bounce()
            
    if 520 < ball.xcor() < 560 and ball.distance(player.opponent) < 30:
        play_sound()
        ball.paddle_bounce()

# Ball missed by left player
    if ball.xcor() < RIGHT_WALL:
        scoreboard.opponent_scores()
        scoreboard.score_up()
        ball.reset()

    # Ball missed by right player
    if ball.xcor() > LEFT_WALL:
        scoreboard.player_scores()
        scoreboard.score_up()
        ball.reset()
        
    if scoreboard.player_score == 7:
        scoreboard.player_won()
        game_is_on = False
    elif scoreboard.opponent_score == 7:
        scoreboard.opponent_won()
        game_is_on = False
    else:
        pass

screen.exitonclick()