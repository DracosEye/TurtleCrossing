import time, random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

turtle = Player()
car_mgr = CarManager()
sb = Scoreboard()

screen.listen()
screen.onkey(turtle.forward, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    rand_car = random.randint(0,5)
    if rand_car == 0:
        car_mgr.new_car()
    car_mgr.move_cars()
    for car in car_mgr.cars:
        if car.distance(turtle) < 22:
            game_is_on = False
            sb.game_over()
            break

    if turtle.crossed:
        car_mgr.speed_up()
        turtle.crossed = False
        sb.level_up()


screen.exitonclick()