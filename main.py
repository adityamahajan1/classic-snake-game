from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time

SPEED = 0.1

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

game_is_on = True
score = 0
while game_is_on:
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase()

    if snake.get_head().xcor() > 290 or snake.get_head().xcor() < -290 or snake.get_head().ycor() > 290 or snake.get_head().ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # for segment in snake.get_segments():
    #     if snake.get_head() == segment:
    #         continue
    #     elif snake.get_head().distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()

    for segment in snake.get_segments()[1:]:
        if snake.get_head().distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    time.sleep(SPEED)
    screen.update()

screen.exitonclick()