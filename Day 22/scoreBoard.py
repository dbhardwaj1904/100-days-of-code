from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.user_two_score = 0
        self.display_score()

    def user_scored(self):
        self.user_score += 1
        self.display_score()

    def user_two_scored(self):
        self.user_two_score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"{self.user_score}", align="center", font=("Arial", 20, "normal"))
        self.goto(100, 260)
        self.write(f"{self.user_two_score}", align="center", font=("Arial", 20, "normal"))
