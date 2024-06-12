from time import time
from turtle import Turtle
from random import randint
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self) -> None:
        self.cars = []
    
    def create_cars(self):
        if randint(1,6) == 1:   
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            rand_x = randint(280,310)
            rand_y = randint(-250,250)
            new_car.goto(rand_x,rand_y)
            new_car.setheading(180)
            self.cars.append(new_car)


    def move_forward(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
                
    def game_over(self):
        for car in self.cars:
            car.clear()
            
