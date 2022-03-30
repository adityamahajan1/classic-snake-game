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

        try:
            with open("data.txt") as file:
                self.high_score = int(file.read())
        except:
            self.high_score = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            try:
                with open("data.txt", "w") as file:
                    file.write(str(self.high_score))
            except:
                file.write(str(0))
        self.score = 0
        self.update_scoreboard()

    def increase(self):
        self.score += 1
        self.update_scoreboard()
