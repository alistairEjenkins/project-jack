from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.speed('fastest')
        self.ball_speed = 0.1
        self.x_move = 10
        self.y_move = 10
        self.move_ball()

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1

    def ball_returned(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def refresh(self):
        self.x_move *= -1
        self.y_move *= -1
        self.goto(0,0)
        self.ball_speed = 0.1
        self.move_ball()