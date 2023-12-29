import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player(x=0, y=-270)
screen.onkey(player.up, "Up")
cars = CarManager()
level_up = Scoreboard()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.move()
    cars.move()
    if cars.turtle.xcor() < 220:
        cars.continue_race()

    if player.ycor() > 250:
        level_up.level_point()
        player.refresh()
        cars.increment()
        print(player.heading())

    # Detect collision
    # NB: Didn't do this particular code myself, encountered some difficulty.
    for car in cars.all_cars:
        if car.distance(player) < 15:
            level_up.game_over()
            game_is_on = False

screen.exitonclick()
