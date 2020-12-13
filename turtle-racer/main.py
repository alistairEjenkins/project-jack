from turtle import Turtle, Screen
from random import randint, choice


def main():
    screen = Screen()
    colors = ['red', 'orange', 'yellow', 'blue', 'brown', 'black']
    racers = []
    for i in range(0,6):
        t = Turtle()
        t.penup()
        t.shape('turtle')
        t.color(colors[i])
        t.goto(-300, 70 - i * 30)
        for _ in range(4):
            t.left(90)
        racers.append(t)

    screen.listen()

    racing = True
    while racing:
        racer = choice(racers)
        racer.forward(randint(1,10))
        if racer.xcor() >= 300:
            print(f'Winner! The {racer.pencolor()} racer is the winner')
            racing = False
    screen.exitonclick()


if __name__ == '__main__':
    main()

#TODO: betting user interaction; button press start; flash winner; start & finish lines