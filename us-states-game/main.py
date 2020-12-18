import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S. State Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
turtle.penup()

t = turtle.Turtle()
t.penup()

found = 0
while found != 50:
    another_state = screen.textinput(title=f'{found} / 50 states found', prompt='Name another state')
    data = pandas.read_csv('50_states.csv')
    for n in range(50):
        if data.iloc[n].state == another_state.title():
            t.goto(data.iloc[n].x, data.iloc[n].y)
            t.write(another_state)
            found += 1






