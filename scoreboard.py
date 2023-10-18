from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.write(f"Level : {self.level}", False, font=FONT)

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", False, font=FONT)

    def game_over(self):
        self.goto(-40,0)
        self.write("Game Over", False, font=FONT)