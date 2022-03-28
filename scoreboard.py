from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(100, 198)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))
        self.goto(-100, 198)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))

    def right_paddle_score(self):
        self.r_score += 1
        self.clear()
        self.goto(100, 198)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))
        self.goto(-100, 198)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))

    def left_paddle_score(self):
        self.l_score += 1
        self.clear()
        self.goto(100, 198)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))
        self.goto(-100, 198)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))










