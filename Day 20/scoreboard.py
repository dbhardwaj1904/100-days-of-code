from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("user_high_score.txt") as high_score_user:
            self.high_score = int(high_score_user.read())
        self.penup()
        self.goto(0, 265)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def user_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Sore: {self.high_score}", align="center", font=("Arial", 18, "normal"))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("user_high_score.txt", mode="w") as final_high_score_user:
                final_high_score_user.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
