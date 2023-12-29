from turtle import Screen
from ball import Ball
from barrier import Barrier
from players import Paddle_
from score_board import Scoreboard

screen = Screen()
screen.title("Pong")
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

barrier = Barrier()
ball = Ball()
score = Scoreboard()
r_paddle = Paddle_(x=-480, y=0)
l_paddle = Paddle_(x=470, y=0)

screen.onkey(r_paddle.up, "a")
screen.onkey(r_paddle.down, "z")

screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.update()
speed_level = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
index = 0
if index > 10:
    index = 0

game_on = True
while game_on:
    screen.tracer(1)
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()
    if ball.distance(l_paddle) < 60 and ball.xcor() > 449 or ball.distance(r_paddle) < 35 and ball.xcor() < -455:
        ball.bounce_ball_x()
        index += 1
        ball.speed(speed_level[index])
    if ball.xcor() > 520:
        ball.next_player()
        ball.bounce_ball_x()
        score.l_point()
        index *= 0
        ball.speed(speed_level[index])
    if ball.xcor() < -500:
        ball.next_player()
        ball.bounce_ball_x()
        score.r_point()
        index *= 0
        ball.speed(speed_level[index])

screen.exitonclick()
