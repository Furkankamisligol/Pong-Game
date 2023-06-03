from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.start_angle()

    def move(self):
        self.fd(3)

    def start_angle(self):
        self.goto(0, 0)
        k = random.randint(-35, 35)
        l = random.randint(145, 215)
        angles = []
        angles.append(k)
        angles.append(l)
        a = random.choice(angles)
        self.seth(a)


"""
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move = -self.y_move
        
        
"""
    