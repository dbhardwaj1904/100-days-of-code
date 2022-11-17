from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
REVERSE_POSITION = (0, 280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def reverse_reset_position(self):
        self.goto(REVERSE_POSITION)

    def move_to_next_leve(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def move_to_previous_level(self):
        if self.ycor() < -280:
            return True
        return False
