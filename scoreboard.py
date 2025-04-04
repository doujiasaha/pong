from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.player_score = 0
        self.opponent_score = 0
        self.write(f"Score: {self.player_score}     Score: {self.opponent_score}", False, align=ALIGNMENT, font=FONT)

    #erase previous score
    def erase(self):
        self.clear()
 
    #print current score       
    def score_up(self):
        self.erase()  
        self.write(f"Score: {self.player_score}     Score: {self.opponent_score}", False, align=ALIGNMENT, font=FONT)
        
    #increase player score
    def player_scores(self):
        self.player_score +=1
    
    #increase opponent score
    def opponent_scores(self):
        self.opponent_score +=1
        
    def player_won(self):
        self.goto(0,0)
        self.write(f"Player won!", False, align=ALIGNMENT, font=FONT)
        
    def opponent_won(self):
        self.goto(0,0)
        self.write(f"Opponent won!", False, align=ALIGNMENT, font=FONT)
        