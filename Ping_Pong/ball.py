from turtle import Turtle


# Make a ball
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1.2, stretch_wid=1.2)
        self.color("white")
        self.speed(1)
        self.y_move = 10
        self.x_move = 10
        # self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_ball_y(self):
        self.y_move *= -1

    def bounce_ball_x(self):
        self.x_move *= -1
        # self.move_speed *= 0.9

    def next_player(self):
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 0)
        self.speed("slowest")
        self.showturtle()
        # self.move_speed = 0.1
