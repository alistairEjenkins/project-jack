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
data = pandas.read_csv('50_states.csv')
found_states = []
while len(found_states) < 50:
    another_state = screen.textinput(title=f'{len(found_states)} / 50 states found', prompt='Name another state')
    another_state = another_state.title()
    if another_state == 'Exit':
        missing_states = [state for state in data.state if state not in found_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv('states_to_learn.csv')
        break
    for n in range(50):
        if data.iloc[n].state == another_state and another_state not in found_states:
            t.goto(data.iloc[n].x, data.iloc[n].y)
            t.write(another_state)
            found_states.append(another_state)

screen.exitonclick()



