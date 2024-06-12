from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        self.player = Turtle("turtle")
        self.player.color("black")
        self.player.setheading(90)
        self.player.penup()
        self.last_pos = (0,0)
        self.player.goto(0,-280)
    def move_forward(self):
        self.player.fd(MOVE_DISTANCE)
    def reset(self):
        self.player.goto(0,-280)
    def get_position(self):
        return self.player.pos()
    def game_over(self):
        self.player.clear()