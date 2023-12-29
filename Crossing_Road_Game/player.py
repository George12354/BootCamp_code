from turtle import Turtle


STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Player(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(x=x, y=y)
        self.setheading(UP)

    def up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.setpos(x=0, y=-270)
        self.setheading(UP)
