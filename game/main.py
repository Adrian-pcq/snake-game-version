from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from obstacle import Obstacle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
obstacle = Obstacle()
obstacle.create()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 283 or snake.head.xcor() < -283 or snake.head.ycor() > 260 or snake.head.ycor() < -283:
        scoreboard.reset()
        obstacle.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            obstacle.reset()
            snake.reset()

screen.exitonclick()