import turtle
from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", False, align=ALIGN, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()