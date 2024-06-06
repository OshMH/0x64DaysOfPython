# first challenge Draw a sqaure

from turtle import Turtle, Screen
import turtle as t
from math import pi
import random
# from turtle import * # this is possible but confusing because we wont know where the classes are coming from.
# import turtle as t

# There are some modules you cant just import.

# second challenge importing 

# bob = Turtle()
# for _ in range(4):
#     for _ in range(20):
#         bob.penup()
#         bob.forward(10)
#         bob.pendown()
#         bob.forward(10)
#     bob.right(90)
  
  
#   # third draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon      
# bob = Turtle()

# def drawShape(sides,bob):
#     angle = 360//sides
#     print(angle)
#     colors:list = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#     bob.color(random.choice(colors))

#     for _ in range(sides):
#         bob.forward(100)
#         angle = angle+(pi/3)
#         bob.right(angle)
        
# for i in range(3,11):
#     drawShape(i,bob)
        

# # Fourth challenge Draw a random walk

# bob = Turtle()
# bob.pensize(10)
# bob.speed(10)
# bobsMoves = ["forward","right","left"]
# colors:list = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# vals = [1,2,3,4,5]
# import math
# ANGLE = 90
# DISTANCE:int = 15

# for _ in range(1000):
#     move = random.choice(bobsMoves)
#     bob.pencolor(random.choice(colors))
#     match move:
#         case "forward":
#             bob.forward(DISTANCE)
#         case "right":
#             bob.right(ANGLE)
#             bob.forward(DISTANCE)
#         case "left":
#             bob.left(ANGLE)
#             bob.forward(DISTANCE)


# # Fifth challenge Draw a spirogrpah
# import math
# bob = Turtle()
# bob.pensize(1)
# bob.speed(0)
# colors:list = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_spirograph(size_of_graph):
#     for i in range(int(360//size_of_graph)):
#         bob.pencolor(random.choice(colors))
        
#         bob.circle(100)
#         bob.setheading(bob.heading()+size_of_graph)
    

# draw_spirograph(2)


# Final challenge draw the spot art?
import colorgram

colors = colorgram.extract('hirstPainting.jpeg',30)
hirstColors =[]
for color in colors:
    temp = []
    for rgb in color.rgb:
        temp.append(rgb)
    hirstColors.append(tuple(temp))



bob = Turtle()
t.colormode(255)
bob.speed(0)
bob.penup()
bob.hideturtle()
bob.speed(0)
DOTS = 100
bob.setheading(225)
bob.forward(250)
bob.setheading(0)
for dot_count in range(1,DOTS+1):
    bob.dot(20,random.choice(hirstColors))
    bob.forward(50)
    
    if dot_count % 10 == 0:    
        bob.setheading(90)
        bob.forward(50)
        bob.setheading(180)
        bob.forward(500)
        bob.setheading(0)

    
    
    
    
        

screen = Screen()
screen.exitonclick()