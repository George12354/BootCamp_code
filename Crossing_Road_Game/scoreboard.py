from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level_score = 1
        self.over = "Game Over"
        self.update_scoreboard()

    def update_scoreboard(self):
        self.speed("fastest")
        self.clear()
        self.goto(-290, 260)
        self.write(f"Level: {self.level_score}", align="left", font=FONT)

    def level_point(self):
        self.level_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(self.over, align="center", font=FONT)
