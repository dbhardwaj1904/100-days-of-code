import turtle as t

turtle = t.Turtle()
screen = t.Screen()


def move_forward():
    turtle.forward(20)


def move_anti_clockwise():
    turtle.setheading(turtle.heading() + 10)


def move_backward():
    turtle.backward(20)


def move_clockwise():
    turtle.setheading(turtle.heading() - 10)


def leave_space():
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()


def clear_screen():
    turtle.penup()
    turtle.clear()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_anti_clockwise, "a")
screen.onkey(move_backward, "s")
screen.onkey(move_clockwise, "d")
screen.onkey(leave_space, "space")
screen.onkey(clear_screen, "c")
screen.exitonclick()
