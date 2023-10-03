import turtle
import time

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) -> None:
        self.snake_arr = []
        self.create_snake(3)
    
    def create_snake(self, snake_length):

        for part in range(snake_length):
            part = turtle.Turtle()
            part.shape("square")
            part.color("white")
            part.penup()
            self.snake_arr.append(part)

        prev_x=self.snake_arr[0].xcor()
        prev_y=self.snake_arr[0].ycor()

        for part in self.snake_arr:
            part.goto(prev_x, prev_y)
            prev_x -= 20

    def move(self):
        for part_no in range(len(self.snake_arr)-1, 0, -1):
            prev_x = self.snake_arr[part_no-1].xcor()
            prev_y = self.snake_arr[part_no-1].ycor()
            self.snake_arr[part_no].goto(prev_x, prev_y)
        self.snake_arr[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.snake_arr[0].heading() != DOWN:
             self.snake_arr[0].setheading(UP)
    
    def down(self):
        if self.snake_arr[0].heading() != UP:
             self.snake_arr[0].setheading(DOWN)
        
    def left(self):
        if self.snake_arr[0].heading() != RIGHT:
             self.snake_arr[0].setheading(LEFT)
    
    def right(self):
        if self.snake_arr[0].heading() != LEFT:
             self.snake_arr[0].setheading(RIGHT)
    

screen = turtle.Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey


screen.exitonclick()

