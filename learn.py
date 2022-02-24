# python high order functions
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
# helps us to start listening for events
screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()

# in the above situation, we have a function that is being used as an input
# Higher order function is a function that can work with other functions, eg onkey is a higher order function in our situation