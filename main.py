import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import car_manager

CARS = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "Up")

score = Scoreboard()


def run_cars():
    new_car = random.randint(1,6)  # Reducing probability of creating new car instead of creating in every loop.
    if new_car == 1:
        car = CarManager()
        CARS.append(car)
        print(f"CARS length : {len(CARS)}")
    for c in CARS:
        if not c.drive():
            CARS.remove(c)


def hit():
    for c in CARS:
        if player.distance(c) < 22:
            return True
    return False


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    run_cars()
    # Completes a level
    if player.ycor() >= player.finish_line:
        score.update()
        player.start_up()
        car_manager.car_speed()
    if hit():
        score.game_over()
        game_is_on = False


screen.exitonclick()