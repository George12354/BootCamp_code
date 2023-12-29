from turtle import Turtle
# STARTING_POSITION
# MOVING_DISTANCE
S_P = [0, -20, -40]
M_D = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segment = []

    def create_snake(self):
        for starting_pos in range(0, 3):
            self.add_segment(starting_pos)

    def add_segment(self, starting_pos):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.forward(S_P[starting_pos])
        self.snake_segment.append(snake)

    def extend(self):
        self.add_segment(0)

    def reset(self):
        for snake_part in self.snake_segment:
            snake_part.goto(1000, 1000)
        self.snake_segment.clear()
        self.create_snake()
        # self.snake_segment[0]

    # This part indicates the snake movement mechanism.
    def move(self):
        for snake_part in range(len(self.snake_segment) - 1, 0, -1):
            # The 3rd parameter is for the "step" and it indicates where it's going to start counting from.
            new_x = self.snake_segment[snake_part - 1].xcor()
            new_y = self.snake_segment[snake_part - 1].ycor()
            self.snake_segment[snake_part].goto(new_x, new_y)
        self.snake_segment[0].forward(M_D)

    def up(self):
        if self.snake_segment[0].heading() != DOWN:
            self.snake_segment[0].setheading(UP)

    def down(self):
        if self.snake_segment[0].heading() != UP:
            self.snake_segment[0].setheading(DOWN)

    def right(self):
        if self.snake_segment[0].heading() != LEFT:
            self.snake_segment[0].setheading(RIGHT)

    def left(self):
        if self.snake_segment[0].heading() != RIGHT:
            self.snake_segment[0].setheading(LEFT)
