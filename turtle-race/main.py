from turtle import Turtle, Screen
from random import randint, shuffle


screen = Screen()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
colors = ["red", "blue", "yellow", "cyan", "green", "orange"]

user_bet = screen.textinput(title="Make your bet", prompt="Which turlte will win the race? Enter a code: ")


class racer_turtles:
    def __init__(self, color, y_offset):
        self.turtle_name = Turtle("turtle")
        self.turtle_name.penup()
        self.turtle_name.color(color)
        self.turtle_name.goto(x=-240, y=-100+y_offset)
    def fd(self):
        self.turtle_name.forward(randint(0,10))
    def get_pencolor(self):
        return self.turtle_name.pencolor()
    def get_xcord(self):
        return self.turtle_name.xcor()

class start_race:
    def __init__(self, all_turtles):
        self.turtles = all_turtles
        self.is_race_on = True
    def start_race(self):
        winning_turtle = None
        while self.is_race_on:
            shuffle(self.turtles)
            for turtle in self.turtles:
                turtle.fd()
                if turtle.get_xcord() > 230:
                    winning_turtle = turtle.get_pencolor()
                    self.is_race_on = False
        if user_bet == winning_turtle:
            print(f"Congratulations, you won the race! with the color {winning_turtle}")
        else:
            print(f"shit, you lost the race, winning turlte is {winning_turtle}")


all_turtles = []
for y_offset,color in enumerate(colors):
    all_turtles.append(racer_turtles(color,y_offset*30))

race = start_race(all_turtles)
race.start_race()

screen.exitonclick()