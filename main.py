import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

snake = Snake()
food = Food()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()
scoreboard = Scoreboard()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food.place()
game_on = True
while game_on:
    scoreboard.update()
    screen.update()
    time.sleep(.05)
    snake.move()
    print(snake.snake[0].pos())
    print(snake.snake[0].pos())
    print(food.piece.pos())
    print("")

    if snake.snake[0].distance(food.piece) < 10:
        food.place()
        snake.extend()
        scoreboard.point()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False

    for piece in snake.snake[1:]:
        if snake.head.distance(piece) < 9:
            print("HIT")
            for x in snake.snake:
                print(x.pos())
            game_on = False

scoreboard.game_over()
screen.exitonclick()