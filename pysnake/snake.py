from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle()
        snake_segment.penup()
        snake_segment.shape('square')
        snake_segment.color('white', 'white')
        snake_segment.goto(position)
        self.segments.append(snake_segment)


    def extend_tail(self):
        position = (self.tail.xcor(),self.tail.ycor())
        self.add_segment(position)

    def move(self):
        for x in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[x - 1].xcor()
            new_y = self.segments[x - 1].ycor()
            self.segments[x].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
