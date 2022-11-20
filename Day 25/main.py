# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)
#     temperatures = []
#     for temperature in data:
#         temperatures.append(int(temperature[1]))
#     print(temperatures)

import turtle
import pandas

states_guessed = 0
states_guessed_array = []
image = "blank_states_img.gif"
states_file = pandas.read_csv("50_states.csv")
total_states = len(states_file)

all_states = states_file.state.to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
screen.setup(height=641, width=725)
turtle.shape(image)

while states_guessed < total_states:
    user_input = screen.textinput(title=f"{states_guessed}/50 are States Correct",
                                  prompt="Enter state name of US?").title()
    if user_input == "Exit" or user_input == "exit":
        missing_states = []
        for state in all_states:
            if state not in states_guessed_array:
                missing_states.append(state)
        missed_states_file = pandas.DataFrame(missing_states)
        missed_states_file.to_csv("Misses_States.csv")
        break
    if user_input in all_states:
        states_guessed_array.append(user_input)
        coord = states_file[states_file.state == user_input]
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(int(coord.x), int(coord.y))
        # state_name.write(state_name.state.item())  // state name from csv file using pandas
        state_name.write(user_input)
        states_guessed = states_guessed + 1
