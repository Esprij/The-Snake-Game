from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier New", 12, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            contents = file.read()
        self.high_score = contents
        self.penup()
        self.ht()
        self.goto(0, 280)
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
