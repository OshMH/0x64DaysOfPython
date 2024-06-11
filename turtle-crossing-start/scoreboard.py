from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(-290,250)
        self.scoreboard.write(f"Level: {self.level}", font=FONT)
    def increment_level(self):
        self.level += 1
        self.scoreboard.clear()
        self.scoreboard.write(f"Level: {self.level}", font=FONT)
        
