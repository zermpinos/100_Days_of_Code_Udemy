from turtle import Turtle, Screen
import random

def create_turtles(colors, y_positions):
    turtles = []
    for color, y_position in zip(colors, y_positions):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(x=-230, y=y_position)
        turtles.append(new_turtle)
    return turtles

def print_result(winning_color, user_bet):
    if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
    else:
        print(f"You've lost! The {winning_color} turtle is the winner!")

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")  # Set the background color to black
user_bet = screen.textinput(title="Make your bet", prompt='Which turtle will win the race? Enter a color: \n "red", "orange", "yellow", "green", "blue", "purple"')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = create_turtles(colors, y_positions)

if user_bet:
    is_race_on = True

FINISH_LINE = 230

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > FINISH_LINE:
            is_race_on = False
            winning_color = turtle.pencolor()
            print_result(winning_color, user_bet)

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
