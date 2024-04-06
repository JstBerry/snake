from turtle import Turtle
import random

class Food():
    def __init__(self):
        self.piece = Turtle("circle")
        self.piece.color("green")
        self.piece.penup()
        self.piece.shapesize(.5)

    def place(self):
        self.piece.goto(x=random.randint(-22, 22)* 10, y=random.randint(-22, 22) * 10)