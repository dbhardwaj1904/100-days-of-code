import turtle as t
import random
# Colors from Image
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

my_turtle = t.Turtle()
t.colormode(255)

color_list = [(38, 217, 68), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10),
              (73, 9, 31), (60, 14, 8), (10, 97, 61), (17, 18, 43), (81, 73, 214), (74, 213, 167), (3, 67, 40)]

my_turtle.hideturtle()
my_turtle.penup()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
number_of_dots = 100

for i in range(1, number_of_dots+1):
    my_turtle.dot(20, random.choice(color_list))
    my_turtle.forward(50)
    if i % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)


my_screen = t.Screen()
my_screen.exitonclick()
