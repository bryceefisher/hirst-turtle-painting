# import colorgram

# colors = colorgram.extract('img.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
from turtle import *
from random import randint
screen = Screen()
screen.colormode(255)
screen.screensize(1000, 1000)

tim = Turtle()
tim.speed("fastest")
tim.pensize(25)
color_list = [(230, 227, 225), (229, 223, 226), (217, 227, 220), (195, 172, 121), (222, 227, 232), (157, 97, 59), (185, 159, 52), (9, 53, 77), (125, 37, 25), (55, 33, 27), (110, 69, 85), (118, 162, 175), (27, 118, 164), (74, 35, 43), (85, 138, 67), (10, 62, 44), (71, 153, 130), (121, 35, 40), (182, 98, 82), (207, 202, 146), (144, 176, 161), (178, 150, 156), (176, 202, 188), (217, 179, 172), (22, 77, 93), (33, 79, 62), (95, 143, 150), (160, 111, 117), (214, 178, 183), (168, 202, 212)]
tim.penup()
tim.goto(-600, -500)
x_axis = -600
y_axis = -500
tim.goto(-600, -500)
dots = 0
while dots < 529:
    for _ in range(23):
        tim.color(color_list[random.randint(0, 29)])
        tim.pendown()
        tim.forward(3)
        tim.penup()
        tim.forward(50)
    y_axis += 50
    tim.goto(x_axis, y_axis)
    dots += 1



screen.exitonclick()






