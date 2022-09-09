from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Monaco", 24, "normal")
FONT2 = ("Monaco", 40, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Monaco", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align=ALIGNMENT, font=FONT2)
