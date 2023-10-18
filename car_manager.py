from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.make_car()

    def make_car(self):
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.penup()
        pos_x = 260
        pos_y = random.randrange(-200, 230, 20)
        self.goto(pos_x, pos_y)
        self.setheading(180)

    def drive(self):
        if self.xcor() <= -350:  # Car has reached to other end
            return False
        self.forward(STARTING_MOVE_DISTANCE)
        return True


def car_speed():
    global STARTING_MOVE_DISTANCE
    STARTING_MOVE_DISTANCE += MOVE_INCREMENT
