import random
import turtle as t

little_turtle = t.Turtle()
t.colormode(255)


def pick_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_picked = (r, g, b)
    return color_picked


little_turtle.speed("fastest")


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        little_turtle.color(pick_color())
        little_turtle.circle(100)
        little_turtle.setheading(little_turtle.heading() + size_of_gap)


draw_spirograph(5)
little_turtle_screen = t.Screen()
little_turtle_screen.exitonclick()
