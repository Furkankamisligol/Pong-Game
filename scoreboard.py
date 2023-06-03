from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.pu()
        self.ht()
        self.goto(position)
        self.score = 0

    def write_score(self):
        self.write(str(self.score), align=ALIGNMENT, font=FONT)
