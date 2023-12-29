from turtle import Turtle


# Make a paddle
class Paddle_(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=3.7, outline=1)
        self.goto(x=x, y=y)
        self.speed("fastest")

    def up(self):
        self.forward(20)

    def down(self):
        self.back(20)
