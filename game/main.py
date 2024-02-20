from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Snake Game')

snake = Snake()

game_on = True
while game_on:
    screen.update()


screen.exitonclick()