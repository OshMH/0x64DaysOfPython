import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
player1=Player()
screen.listen()
screen.onkey(fun=player1.move_forward,key="w")
scoreboard = Scoreboard()

car_manager = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_forward()
