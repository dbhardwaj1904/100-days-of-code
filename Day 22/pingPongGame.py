from turtle import Screen
from paddle import Paddle
from pongBall import PongBall
from scoreBoard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

user_paddle = Paddle((-350, 0))
user_two_paddle = Paddle((350, 0))
ball = PongBall()
score = ScoreBoard()

screen.listen()
screen.onkey(user_paddle.move_up, "w")
screen.onkey(user_paddle.move_down, "s")
screen.onkey(user_two_paddle.move_up, "Up")
screen.onkey(user_two_paddle.move_down, "Down")

gameOn = True
while gameOn:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move_ball()

    # Collision with wall for re-bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()

    # Collision with user_two_paddle
    if ball.distance(user_two_paddle) < 60 and ball.xcor() > 320\
            or ball.distance(user_paddle) < 40 and ball.xcor() > -340:
        ball.bounce_ball_x()

    # user_two_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.user_scored()

    # user misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.user_two_scored()

screen.exitonclick()
