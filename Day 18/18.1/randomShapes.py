import turtle as t

my_turtle = t.Turtle()

my_turtle.shape("arrow")
angle = 360
start_shape = 2
number_of_shapes = 6

for i in range(number_of_shapes):
    start_shape += 1
    for j in range(0, start_shape):
        my_turtle.forward(100)
        my_turtle.right(angle/start_shape)

screen = t.Screen()
screen.exitonclick()
