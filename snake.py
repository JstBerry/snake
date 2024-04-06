from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_piece = None
        self.snake_pos_x = 0
        self.snake_pos_y = 0
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for x in range(1, 4):
            self.snake_piece = Turtle(shape="square")
            self.snake_piece.color("white")
            self.snake_piece.penup()
            self.snake_piece.shapesize(.5)
            self.snake_piece.goto(self.snake_pos_x, 0)
            self.snake_pos_x -= 10
            self.snake.append(self.snake_piece)

    def move(self):
        for x in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[x - 1].xcor()
            new_y = self.snake[x - 1].ycor()
            self.snake[x].goto(new_x, new_y)
        self.snake[0].forward(10)

    def add_piece(self, position):
        self.snake_piece = Turtle(shape="square")
        self.snake_piece.penup()
        self.snake_piece.color("white")
        self.snake_piece.shapesize(.5)
        self.snake_piece.goto(position)
        self.snake.append(self.snake_piece)

    def extend(self):
        self.add_piece(self.snake[-1].position())

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
