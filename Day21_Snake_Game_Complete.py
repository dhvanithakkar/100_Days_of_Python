import turtle
import time
import random

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

GAP = 20
WIDTH = 600
HEIGHT=600

class Snake:

    def __init__(self, colour_choice) -> None:
        self.snake_arr = []
        self.colour_count = 0
        self.colours = self.get_palette(colour_choice)

        self.create_snake(3)
    
    def create_snake(self, snake_length):

        for part in range(snake_length):
            part = turtle.Turtle()
            part.shape("square")
            part.color(self.colours[self.colour_count])
            
            self.colour_count = (self.colour_count + 1) % len(self.colours)
            
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

    def increase_length(self):
        part = turtle.Turtle()
        part.shape("square")
        part.color(self.colours[self.colour_count])
        
        self.colour_count = (self.colour_count + 1) % len(self.colours)
        
        part.penup()
        self.snake_arr.append(part)
        prev_x = self.snake_arr[-2].xcor()
        prev_y = self.snake_arr[-2].ycor()
        self.snake_arr[-1].goto(prev_x, prev_y)
    
    def get_palette(self, colour_choice):
        if colour_choice.lower()[0] == 'r':
            return ['red']
        elif colour_choice.lower()[0] == 'w':
            return ['white']
        elif colour_choice.lower()[0] == 'o':
            return ['orange']
        elif colour_choice.lower()[0] == 'c':
            return ['#d8f8e2', '#e4c1f9', '#f694c1', '#ede7b1', '#a9def9']
        elif colour_choice.lower() == 'green':
            return ['green']
        else:
            return ['grey', 'white']


FOOD_COLOURS = ['green', '#d2b48c', 'blue']

    
class Food(turtle.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color(random.choice(FOOD_COLOURS))
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-(WIDTH/2-GAP-10), WIDTH/2-GAP-10)
        random_y = random.randint(-(HEIGHT/2-GAP-10), HEIGHT/2-GAP-10)
        self.color(random.choice(FOOD_COLOURS))
        self.goto(random_x, random_y)


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, (HEIGHT)/2-50 )
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Your score is : {self.score}", align="center", font = ("Arial", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.print_score()
    
    def game_over(self):
        self.goto(0,0)
        self.print_score()

screen = turtle.Screen()

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


inp_screen = turtle.Screen()
inp_screen.setup(width=WIDTH, height=HEIGHT)
colour_choice = inp_screen.textinput(title="Snake Colours", prompt="Options: Red, Green, White, Candy, Orange and Grey/white\nChoose the snake colour you want: ")


snake = Snake(colour_choice)
food = Food()
screen.listen()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    #so that graphics are not messy
    time.sleep(0.1)
    screen.update()
    
    # Movement
    snake.move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Eat food
    if snake.snake_arr[0].distance(food)<15:
        scoreboard.increase_score()
        snake.increase_length()
        food.refresh()

    # Wall collision
    if snake.snake_arr[0].xcor() >= (WIDTH/2-GAP) or snake.snake_arr[0].xcor() <= -(WIDTH/2-GAP) or snake.snake_arr[0].ycor() >= (HEIGHT/2-GAP) or snake.snake_arr[0].ycor() <= -(HEIGHT/2-GAP):
        scoreboard.game_over()
        game_is_on = False
    
    # Tail collision
    for part in snake.snake_arr[1:]:
        if snake.snake_arr[0].distance(part) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()

