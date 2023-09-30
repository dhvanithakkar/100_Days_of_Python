# # 1.Timmy the Turtle : Basic
# from turtle import Turtle
# import turtle
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOrchid")
# timmy.forward(100)
# my_screen = turtle.Screen()

# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()


# # 2. Dotted lines to make a square
# import turtle as t
# timmy = t.Turtle()

# timmy.shape("turtle")
# timmy.color("DarkOrchid")

# for _ in range(4):
#     timmy.left(90)
#     for i in range(5):
#         timmy.penup()
#         timmy.forward(10)
#         timmy.pendown()
#         timmy.forward(10)

# my_screen = t.Screen()
# my_screen.exitonclick()

# # 3. Overlay/draw regular polygons from triangle to decagon and give random colour to each

# import turtle as t
# import random
# timmy = t.Turtle()

# timmy.shape("turtle")
# timmy.color("DarkOrchid")

# colours = ["deep pink", "purple", "blue", "turquoise", "black", "silver"]

# for sides in range(3, 11):
#     angle = 360/sides
#     print(sides)
#     timmy.pencolor(random.choice(colours))
#     for side in range(sides):
#         timmy.right(angle)
#         timmy.forward(100)

# my_screen = t.Screen()
# my_screen.exitonclick()


# # 4. Random path with random colours

# import turtle as t
# import random
# timmy = t.Turtle()
# t.colormode(255)

# timmy.speed("fastest")
# timmy.hideturtle()

# directions = [0, 90, 180, 270]
# # or use colours = ["deep pink", "purple", "blue", "turquoise", "black", "silver"] and then random.choice(colours)
# timmy.pensize(15)

# for movements in range(1000):
#     timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     timmy.setheading(random.choice(directions))    
#     timmy.forward(30)

# my_screen = t.Screen()
# my_screen.exitonclick()

# # 5. Draw a spirograph

# import turtle as t
# import random
# timmy = t.Turtle()
# t.colormode(255)

# timmy.speed("fastest")
# timmy.hideturtle()
# gap = 5
# colours = ["deep pink", "purple", "blue", "turquoise", "black", "silver"]

# for sides in range(360//gap):
#     timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     timmy.circle(100)
#     timmy.setheading(timmy.heading() + gap)


# my_screen = t.Screen()
# my_screen.exitonclick()


# # Final Project, Hirst Dot Paintings
# import colorgram
# colors = colorgram.extract("Hirst_painting.jpg", 10)
# colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
# print(colors)

colors = [(236, 240, 244), (243, 248, 246), (200, 172, 111), (154, 180, 195), (193, 162, 177), (153, 185, 174), (214, 204, 117), (208, 180, 196)]

import turtle as t
import random

GRID = 10
GAP = 30
SIZE = 10

timmy = t.Turtle()
timmy.penup()
t.colormode(255)
timmy.setheading(225)
timmy.forward(GAP*SIZE/2)
timmy.setheading(0)
timmy.hideturtle()


timmy.speed("fast")




for row in range(GRID):
    for columns in range(GRID):
        timmy.pencolor(random.choice(colors))
        timmy.dot(SIZE)
        timmy.forward(GAP)
    if row %2 == 0: 
        timmy.left(90)
        timmy.forward(GAP)
        timmy.left(90)
        timmy.forward(GAP)
    else: 
        timmy.right(90)
        timmy.forward(GAP)
        timmy.right(90)
        timmy.forward(GAP)

my_screen = t.Screen()
my_screen.exitonclick()