import random
import turtle
from turtle import Turtle, Screen
# import colorgram
# colors = colorgram.extract('Damien Hirst spot painting.jpg', 35)
#
# # first_color = colors[0]
# # print(first_color)
# # print(colors)
# # rgb = first_color.rgb
# # hsl = first_color.hsl
# # proportion = first_color.proportion
# # print(f"rgb:{rgb} hsl:{hsl} proportion:{proportion}")
# # The code demonstrate shows the different approach of accessing the rgb, hsl and proportion, for more visit the
# # package documentation from pypi
# color_rgb = []
# for color_ in colors:
#     r = color_.rgb.r
#     g = color_.rgb.g
#     b = color_.rgb.b
#     new_color = (r, g, b)
#     color_rgb.append(new_color)
# print(color_rgb)

color_list = [(232, 227, 214), (218, 218, 223), (108, 110, 127), (214, 153, 89), (140, 141, 152), (196, 59, 24),
              (227, 214, 103), (234, 217, 226), (225, 235, 227), (180, 159, 39), (99, 108, 177), (211, 145, 178),
              (29, 46, 27),
              (27, 26, 70), (199, 18, 5), (37, 40, 18), (227, 167, 198), (221, 81, 52), (43, 45, 106), (126, 84, 96),
              (217, 75, 99),
              (232, 173, 161), (87, 100, 90), (182, 184, 213), (188, 14, 21), (153, 165, 157), (222, 206, 23),
              (48, 27, 50),
              (73, 72, 38), (51, 72, 53), (182, 198, 185), (115, 134, 125), (175, 199, 204), (117, 131, 134),
              (47, 70, 73)]

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)
tim.color("black", "green")
my_screen = Screen()
tim.penup()
tim.speed("fastest")
tim.hideturtle()
tim.setpos(-300, -300)
for spot in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.fd(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.penup()
    for jump in range(10):
        tim.fd(50)
    tim.right(90)
    tim.right(90)
    tim.pendown()
my_screen.exitonclick()
