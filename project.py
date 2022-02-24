from turtle import Turtle, Screen, turtles
import random

# turtle = Turtle('turtle')
screen = Screen()
screen.setup(width=500, height=400)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_bet = screen.textinput(title="Make Your Bet", prompt=f"Which turtle will win the race?? {', '.join(colors)}? Enter a color: ")

while user_bet not in colors:
    user_bet = screen.textinput(title="Make Correct Bet", prompt=f"Which turtle will win the race??? {', '.join(colors)} Enter a correct color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turles = []


y_cor = -110
for col in colors:
    turtle = Turtle('turtle')
    turtle.penup()
    turtle.color(col)
    turtle.goto(x=-230, y=y_cor)
    turles.append(turtle)
    y_cor += 55

race_on = True

while race_on:
    for turtle in turles:
        if turtle.xcor() > 210:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won! The {winning_color} turtle is the winner")
            else:
                print(f"you lost! The {winning_color} turtle is the winner")
            race_on = False
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)
screen.exitonclick()