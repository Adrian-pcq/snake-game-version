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
levels = []

choice = screen.textinput("Choose a game mode", "Type 'classic' or 'adan'").lower()

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

    if choice == 'adan':
        if scoreboard.score % 5 == 0 and scoreboard.score != 0 and scoreboard.score not in levels:
            for _ in range(2):
                obstacle.create()
                if obstacle.distance(food):
                    food.refresh()
            levels.append(scoreboard.score)

        for odd in obstacle.all:
            if snake.head.distance(odd) < 15:
                scoreboard.reset()
                obstacle.reset()
                levels.clear()
                snake.reset()

    if snake.head.xcor() > 283 or snake.head.xcor() < -283 or snake.head.ycor() > 260 or snake.head.ycor() < -283:
        scoreboard.reset()
        obstacle.reset()
        levels.clear()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            obstacle.reset()
            levels.clear()
            snake.reset()

screen.exitonclick()