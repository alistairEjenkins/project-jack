from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,player):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid= 5,stretch_len= 1)
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.isvisible= False
        if player == 'one':
            self.goto(-350, 0)
        else:
            self.goto(350,0)
        self.isvisible = True

    def move_up(self):

        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)