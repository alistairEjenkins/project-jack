import turtle
from random import randint
import colorgram

def main():

    screen = turtle.Screen()
    screen.screensize(200, 267)

    colors = colorgram.extract('image.jpg', number_of_colors=84)
    print(colors)

    t = turtle.Turtle()
    t.penup()
    t.setpos(-222,-134)
    t.pendown()
    t.pensize(10)

    x_size = 444
    y_size = 268
    x_dots = 12
    y_dots = 7
    x_step = x_size/x_dots
    y_step = y_size/y_dots
    rotate = 90
    turtle.colormode(255)
    #print(choice(colors))
    for _ in range(y_dots):
        for x in range(x_dots):
            t.pencolor(colors[randint(0,len(colors)-1)].rgb)
            t.dot()
            t.penup()
            if x != 11:
                t.forward(x_step)
                t.pendown()
            else:
                t.left(rotate)
                t.forward(y_step)
                t.left(rotate)
                rotate *= -1

    screen.exitonclick()

if __name__ == '__main__':
   main()