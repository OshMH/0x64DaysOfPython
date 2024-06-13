from turtle import Turtle

class StateNamer():
    def __init__(self):
        self.list_of_names = []
        self.FONT = ("Courier", 24, "normal")
    def name_state(self, name, x, y):
        new_name = Turtle()
        new_name.penup()
        new_name.hideturtle()
        new_name.goto(x,y)
        new_name.write(name)
        self.list_of_names.append(new_name)


