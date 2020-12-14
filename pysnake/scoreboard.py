from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pen(shown=False)
        self.goto(0,y=260)
        self.color('white')
        self.pendown()
        self.score = 0

    def update_score(self):
        self.clear()
        self.write(f'Score {self.score}', align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
        

