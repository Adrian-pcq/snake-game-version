from turtle import Screen

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Snake Game')

game_on = True
while game_on:
    screen.update()


screen.exitonclick()