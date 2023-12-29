from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt") as score_sheet:
            contents = score_sheet.read()
            self.high_score = int(contents)
        # I will read here

    def score_dashboard(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Courier', 12, 'normal'))

    def score_mark(self, mark):
        self.clear()
        self.score += mark

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Courier', 12, 'normal'))
        with open("data.txt", mode="w") as score_sheet:
            score_sheet.write(f"{self.high_score}")

        # then I will write here

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, "center", ('Courier', 12, 'normal'))
