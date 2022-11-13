from turtle import Screen

screen = Screen()

screen.setup(width=800, height=800)
screen.tracer(0)

screen.listen()
screen.onkey("Up")
screen.onkey("Down")

screen.exitonclick()
