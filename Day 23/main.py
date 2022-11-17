from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move_car()

    # Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score.game_over()

    if player.move_to_next_leve():
        player.reset_position()
        car_manager.level_up()
        score.score_up()

    if player.move_to_previous_level():
        player.reverse_reset_position()
        score.score_down()


screen.exitonclick()
