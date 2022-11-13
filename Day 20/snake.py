import turtle as t

SNAKE_POSITION = [(0, 0), (-20, 0), (20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in SNAKE_POSITION:
            self.add_mini_snake(i)

    def move(self):
        for mini_snake in range((len(self.snake) - 1), 0, -1):
            x = self.snake[mini_snake - 1].xcor()
            y = self.snake[mini_snake - 1].ycor()
            self.snake[mini_snake].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def add_mini_snake(self, i):
        mini_snake = t.Turtle("square")
        mini_snake.color("white")
        mini_snake.penup()
        mini_snake.goto(i)
        self.snake.append(mini_snake)

    def extend(self):
        self.add_mini_snake(self.snake[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
