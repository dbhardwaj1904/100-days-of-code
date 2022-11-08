import random
import turtle as t

screen = t.Screen()
screen.setup(width=500, height=400)
user = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color of turtle: ")

colors = ["red", "orange", "yellow", "green", "purple", "blue"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle_index in range(0, 6):
    turtle = t.Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(turtle)

start_race = False
if user:
    start_race = True

while start_race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            start_race = False
            winner = turtle.pencolor()
            if winner == user:
                print("You won!")
            else:
                print(f"Sorry you lost, better luck next time. Winner is {winner}")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
