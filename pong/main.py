from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from time import sleep

def main():

    screen = Screen()
    screen.setup(800,600)
    screen.bgcolor('black')
    screen.tracer(0)

    paddle_1 = Paddle('one')
    paddle_2 = Paddle('two')
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(paddle_1.move_up,'w')
    screen.onkey(paddle_1.move_down, 's')
    screen.onkey(paddle_2.move_up, 'Up')
    screen.onkey(paddle_2.move_down, 'Down')
    scoreboard.update_score()

    playing = True
    while playing:
        sleep(0.1)
        ball.move_ball()
        screen.update()

        # collision with top/bottom
        if ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.bounce()

        # collision with paddle
        if (paddle_1.distance(ball) <= 50 and ball.xcor() < - 340) or \
                (paddle_2.distance(ball) <= 50 and ball.xcor() > 340):
            ball.ball_returned()


        # score a point
        if ball.xcor() <=-400:
            scoreboard.score_2 += 1
            ball.refresh()
        elif ball.xcor() >=400:
            scoreboard.score_1 +=1
            ball.refresh()
        scoreboard.update_score()


        if scoreboard.score_1 == 11 or scoreboard.score_2 == 11:
            scoreboard.game_over()
            playing = False

    screen.exitonclick()

if __name__ == '__main__':
    main()