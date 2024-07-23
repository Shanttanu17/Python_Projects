from turtle import Turtle

SNAKE_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:

    def __init__(self):
        self.segment = []
        self.make_snake()
        self.head = self.segment[0]

    def make_snake(self):
        for position in SNAKE_POSITIONS:
            new_segment = Turtle()
            new_segment .color("white")
            new_segment .shape("square")
            new_segment .penup()
            new_segment .goto(position)
            self.segment.append(new_segment)



    def move_snake(self):
        for seg_num in range(len(self.segment)-1, 0, -1):
            seg_xcor = self.segment[seg_num - 1].xcor()
            seg_ycor = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(seg_xcor, seg_ycor)
        self.segment[0].forward(MOVE_DISTANCE)

    def move_left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def move_right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def move_up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def move_down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)
    