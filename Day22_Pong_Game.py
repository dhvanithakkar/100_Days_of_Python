"""create screen and paddles, scoreboard, ball
figure out how to move paddles
figure out how ball moves

check for ball out of bounds
keep score
"""

import turtle
import random
import time

MOVE_DISTANCE = 10

LINE_LEN = 10
GAP=20
WIDTH = 800
HEIGHT = 600

class Paddle(turtle.Turtle):
    def __init__(self, location) -> None:
        super().__init__()
        self.create_paddle()
        self.reset(location)
        
    def create_paddle(self):
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
    
    def reset(self, location):
        if location.lower() == "right":
            self.goto(WIDTH/2-20, 0)
        elif location.lower() == "left":
            self.goto(-(WIDTH/2-20), 0)
        
        self.setheading(0)
    
    def up(self):
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def down(self):
        self.goto(self.xcor(), self.ycor()-MOVE_DISTANCE)


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, (HEIGHT)/2-50 )
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"{self.left_score}      {self.right_score}", align="center", font = ("Arial", 24, "normal"))
    
    def final_score(self):
        self.goto(0,0)
        if self.left_score > self.right_score:
            winner = "Left"
        else:
            winner = "Right"
        
        self.write(f"{winner} Wins!! Final score: {self.left_score}|{self.right_score}", align="center", font = ("Arial", 24, "normal"))



class Ball(turtle.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

        self.left_score = 0
        self.right_score = 0

    def collided_with_wall(self):
        if self.ycor() >= (HEIGHT/2-GAP) or self.ycor() <= -(HEIGHT/2-GAP):
            return True
        return False
    
    def wall_collision(self):
        self.y_move *= -1

    def paddle_collision(self):
        self.x_move *= -1
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset(self):
        self.goto(0,0)



class Center_line(turtle.Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.setheading(270)
        self.hideturtle()
        self.make_line()
    
    def make_line(self):
        self.penup()
        self.goto(0, HEIGHT/2)
        while self.ycor() >= -(HEIGHT/2-LINE_LEN):
         
            self.penup()
            self.forward(LINE_LEN)
            self.pendown()
            self.forward(LINE_LEN)
            


screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball=Ball()
scoreboard = Scoreboard()

screen.listen()
center_line = Center_line()

SLEEP_TIME = 0.1
game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    if SLEEP_TIME > 0.0000002:
        SLEEP_TIME -= 0.0000002
    
    # Wall collision
    if ball.collided_with_wall():
        ball.wall_collision()

    # Moving paddles
    ball.move()
    screen.onkeypress(left_paddle.up, "w")
    screen.onkeypress(left_paddle.down, "s")
    screen.onkeypress(right_paddle.up, "Up")
    screen.onkeypress(right_paddle.down, "Down")
    
    # Paddle collision
    if ball.distance(right_paddle) < 50 and right_paddle.xcor() - ball.xcor() < 15:
        ball.paddle_collision()
    
    elif ball.distance(left_paddle) < 50 and ball.xcor() - left_paddle.xcor() < 15:
        ball.paddle_collision()

    # Exceeds bounds
    if ball.xcor() >= (WIDTH/2-GAP):
        scoreboard.left_score += 1
        SLEEP_TIME = 0.1
        ball.reset()
        left_paddle.reset("left")
        right_paddle.reset("right")
    
    if ball.xcor() <= -(WIDTH/2-GAP):
        scoreboard.right_score += 1
        SLEEP_TIME = 0.1
        ball.reset()
        left_paddle.reset("left")
        right_paddle.reset("right")

    scoreboard.print_score()

    # Best of 5
    if scoreboard.right_score + scoreboard.left_score == 5:
        scoreboard.final_score()
        game_is_on = False



screen.exitonclick()