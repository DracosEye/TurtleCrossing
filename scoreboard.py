from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(x=-280, y=270)
        self.level_up()

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(x=-0, y=0)
        self.write(arg="GAME OVER", align="center", font=FONT)