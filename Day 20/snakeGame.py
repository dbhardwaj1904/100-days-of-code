from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Caught Food
    if snake.head.distance(food) < 15:
        food.food_location()
        snake.extend()
        score.user_score()

    # Detect wall hit
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset_game()
        snake.reset_snake()

    # Hit itself
    for i in snake.snake[1:]:
        if snake.head.distance(i) < 10:
            score.reset_game()
            snake.reset_snake()

screen.exitonclick()
