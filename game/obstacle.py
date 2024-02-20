from turtle import Turtle
import random


class Obstacle(Turtle):
    def __init__(self) -> None:
        self.all = []

    def create(self):
        odd = Turtle('turtle')
        odd.color('red')
        odd.penup()
        odd.speed('fastest')
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        odd.goto(random_x, random_y)
        self.all.append(odd)

    def reset(self):
        for odd in self.all:
            odd.goto(1000, 1000)
        self.all.clear()

    def distance(self, food):
        for odd in self.all:
            return odd.distance(food)<20
