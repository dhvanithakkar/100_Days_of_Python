from turtle import Turtle, Screen
import time
import random

red = Turtle()
red.color("red")

orange = Turtle()
orange.color("orange")

yellow = Turtle()
yellow.color("yellow")

green = Turtle()
green.color("green")

blue = Turtle()
blue.color("blue")

indigo = Turtle()
indigo.color("indigo")

violet = Turtle()
violet.color("violet")

width = 500
height = 400
gap = 20

screen = Screen()
screen.setup(width, height)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter colour: ")
print(f"Your bet is {bet}")
all_turtles = [red, orange, yellow, green, blue, indigo, violet]

y_coordinate = len(all_turtles)//2*gap
leading_position = -width/2

# create finish flag
flag = Turtle("square")
flag.penup()
flag.hideturtle()
flag.speed("fastest")

line_x = width/2- 40
line_y = height/2 - gap
finishing_x = line_x

while line_y-20 >= -(height/2-gap):
    flag.goto(line_x, line_y)
    flag.stamp()
    line_x += 20
    line_y -= 20
    flag.goto(line_x, line_y)
    flag.stamp()
    line_x -= 20
    line_y -= 20
    flag.goto(line_x, line_y)
    flag.stamp()


if len(all_turtles)%2 != 0:
    y_coordinate -=  gap/2

for turt in all_turtles:
    turt.shape("turtle")
    turt.speed("fastest")

for turt in all_turtles:
    turt.penup()
    turt.goto((-width/2+10), y_coordinate)
    y_coordinate -= gap


def move_forwards(turt):
    time.sleep(1)
    turt.forward(50)

while True:
    moving_turtle = random.choice(all_turtles)
    move_forwards(moving_turtle)

    if moving_turtle.xcor() >= finishing_x:
        winner = moving_turtle
        break
        turtle.forward(rand_distance)
    
    if moving_turtle.xcor() > leading_position:
        leading_position = moving_turtle.xcor()
        for turt in all_turtles:
            turt.shapesize(1, 1, 1)
        
        moving_turtle.shapesize(1.5, 1.5, 1)



if bet == str(winner.color()[0]):
    print(f"You won!! Your bet {bet} won the race.")
else:
    print(f"You lost! {str(winner.color()[0]).title()} won the race.")

screen.exitonclick()