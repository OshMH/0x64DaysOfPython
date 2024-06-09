from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

TURNING_CONSTANT = 10
MOVING_CONSTANT = 10
def move_forwards():
    tim.forward(MOVING_CONSTANT)
    
def move_anti_clockwise():
    tim.left(TURNING_CONSTANT)
def move_clockwise():
    tim.right(TURNING_CONSTANT)
def clear_screen():
    screen.reset()
    
def move_backwards():
    tim.backward(MOVING_CONSTANT)
    
    
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_anti_clockwise)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="e", fun=exit)
screen.exitonclick()

# Sending functions into other functions is called higher order functions

