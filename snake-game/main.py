from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


class Snake:
    starting_positions = [ (0,0),(20,0),(-20,0)]
    def __init__(self):
        self.segments = []   
        for seg in self.starting_positions:
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(seg)
            self.segments.append(new_seg)
        time.sleep(0.5)
        screen.update()


class Snake_game:
    game_is_on = True
    def __init__(self,snaky:Snake):
        while self.game_is_on:
            for seg in snaky.segments:
                seg.forward(10)
            time.sleep(0.1)
            screen.update()


snaky = Snake()
game = Snake_game(snaky)

# Stopping at 10:05 of 186 and going to day 24





















screen.exitonclick()