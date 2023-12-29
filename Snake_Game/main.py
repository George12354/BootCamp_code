from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score
import time


screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
snake.create_snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score_no = 0
    score.score_dashboard()

    # Detect collision with food.
    if snake.snake_segment[0].distance(food) < 15:
        food.refresh()
        score_no += 1
        score.score_mark(score_no)
        snake.extend()

    # Detect collision with wall.
    if (snake.snake_segment[0].xcor() > 290 or snake.snake_segment[0].xcor() < -290 or snake.snake_segment[0].ycor() >
            290 or snake.snake_segment[0].ycor() < -290):
        score.reset()
        snake.reset()

    # Detect collision with tail.
    for current_segment in snake.snake_segment[1:]:
        if snake.snake_segment[0].distance(current_segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
