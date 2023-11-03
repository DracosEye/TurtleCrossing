from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:

    def __init__(self):
        self.cur_move_dist = STARTING_MOVE_DISTANCE
        self.cars = []

    def move_cars(self):
        for car in self.cars:
            car.setx(car.xcor() - self.cur_move_dist)
            if car.xcor() < -330:
                self.cars.remove(car)

    def new_car(self):
        car = Turtle(shape="square")
        car.penup()
        car.color(random.choice(COLORS))
        car.shapesize(stretch_len=3, stretch_wid=1)
        ypos = random.randrange(-250, 260)
        car.goto(300, ypos)
        self.cars.append(car)

    def speed_up(self):
        self.cur_move_dist += MOVE_INCREMENT
