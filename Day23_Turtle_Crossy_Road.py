import time
import turtle
import random

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


WIDTH = 600
HEIGHT = 600

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reset(self):
        self.goto(STARTING_POSITION)

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-((WIDTH)/2-100), (HEIGHT)/2-50 )
        self.print_level()

    def print_level(self):
        self.clear()
        self.write(f"Level : {self.level+1}", align="center", font = FONT)
    
    def next_level(self):
        self.level += 1
        self.print_level()
    
    def game_over(self):
        self.goto(0,0)
        self.print_level()

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager:
    def __init__(self) -> None:
        self.car_array = []
        self.new_cars()
    
    def new_cars(self):
        for _ in range(random.choice([0, 0, 0, 0, 0, 0, 1])):
            car = turtle.Turtle()
            car.penup()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.setheading(180)
            y_coordinate = random.randint(-250, 250)
            car.goto(WIDTH/2, y_coordinate)
            self.car_array.append(car)

    def move(self, level):
        for car in self.car_array:
            car.forward(STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT)

screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

player = Player()
cars = CarManager()

scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.listen()
    screen.onkeypress(player.move, "space")
    cars.move(scoreboard.level)

    cars.new_cars()

    for car in cars.car_array:
        if (player.distance(car) < 30 and player.ycor() - car.ycor() < 15) or player.distance(car) < 10:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.next_level()
        player.reset()
    
screen.exitonclick()