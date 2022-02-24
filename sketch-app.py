from turtle import Turtle, Screen, back, forward
# w= forward
# s= back
# a = counter-clockwise
# d = clockwise
# c = clear drawing

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)

def move_back():
    turtle.back(10)

def move_counter_clockwise():
    turtle.setheading(turtle.heading()+10)

def move_clockwise():
    turtle.setheading(turtle.heading()-10)

def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='a', fun=move_counter_clockwise)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()