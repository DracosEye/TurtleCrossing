from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player (Turtle):

    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.crossed = False

    def forward(self):
        self.sety(self.ycor() + MOVE_DISTANCE)
        if self.ycor() > FINISH_LINE_Y:
            self.crossed = True
            self.goto(STARTING_POSITION)