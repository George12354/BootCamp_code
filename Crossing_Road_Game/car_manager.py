import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.start = STARTING_MOVE_DISTANCE
        for index in range(6):
            for turtle_index in range(2):
                x = random.randint(0, 300)
                y = random.randint(-240, 250)
                self.turtle = Turtle(shape="square")
                self.turtle.penup()
                self.turtle.shapesize(stretch_wid=0.7, stretch_len=1.5, outline=0)
                self.turtle.setpos(x=x, y=y)
                self.turtle.color(COLORS[index])
                self.all_cars.append(self.turtle)

    def continue_race(self):
        for index in range(6):
            for turtle_index in range(1):
                x = random.randint(300, 300)
                y = random.randint(-240, 250)
                self.turtle = Turtle(shape="square")
                self.turtle.penup()
                self.turtle.shapesize(stretch_wid=0.7, stretch_len=1.5, outline=0)
                self.turtle.setpos(x=x, y=y)
                self.turtle.color(COLORS[index])
                self.all_cars.append(self.turtle)

    def move(self):
        for moving_car in self.all_cars:
            moving_car.back(self.start)

    def increment(self):
        self.start += MOVE_INCREMENT
