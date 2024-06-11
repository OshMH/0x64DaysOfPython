from turtle import Turtle
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self) -> None:
        self.cars = []
        for color in COLORS:
            for _ in range(3):
                new_car = Turtle("square")
                new_car.color(color)
                new_car.penup()
                rand_x = randint(280,310)
                rand_y = randint(-280,280)
                
            new_car.goto(randint(280,310),randint(-280,280))
            new_car.setheading(180)
            self.cars.append(new_car)
            
    def move_forward(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
