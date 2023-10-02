from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)
    
def restart():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=restart)
screen.exitonclick()

'''
# Code by Fabian in the comments. Helps in double key press but does not offer clear function and is not that well written. Try for this.
import turtle
 
# Dictionary containing pairings of keyboard keys and tuples with a boolean if the key is pressed
# and a function to execute if it is
pressed_keys = {}
 
# How often to check for keys pressed, in ms
CHECKING_INTERVAL = 10
 
# How fast to move and turn per check
SPEED = 10
TURNING_SPEED = 15
 
 
def down(key):
    def inner():
        pressed_keys[key]["pressed"] = True
 
    return inner
 
 
def up(key):
    def inner():
        pressed_keys[key]["pressed"] = False
 
    return inner
 
 
def register_keys(screen, key_function_tuples):
    """
    Registers key/function-pairs to the screen object, to enable 'hold-down'-functionality for keyboards without native support
    """
    for key_function in key_function_tuples:
        # Extract key and function of the tuple
        k, f = key_function
        pressed_keys[k] = {"pressed": False, "function": f}
 
        # Get closure functions to preserve the context of this loop, most notably the key,
        # and simultaneously create dummy functions that do not need an argument
        d = down(k)
        u = up(k)
 
        screen.onkeypress(d, k)
        screen.onkeyrelease(u, k)
 
 
def key_loop(screen):
    """Check every {CHECKING_INTERVAL} milliseconds, which keys are pressed and execute functions accordingly"""
    for key in pressed_keys:
        pressed = pressed_keys[key]["pressed"]
        func = pressed_keys[key]["function"]
        if pressed:
            func()
    screen.ontimer(lambda: key_loop(screen), CHECKING_INTERVAL)
 
 
screen = turtle.Screen()
turtle.speed("fastest")
register_keys(
    screen,
    [
        ('w', lambda: turtle.forward(SPEED)),
        ('s', lambda: turtle.backward(SPEED)),
        ('d', lambda: turtle.right(TURNING_SPEED)),
        ('a', lambda: turtle.left(TURNING_SPEED)),
    ]
)
screen.listen()
key_loop(screen)
screen.mainloop()
'''