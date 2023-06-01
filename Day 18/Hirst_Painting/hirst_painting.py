import turtle as turtle_module
import random

DOT_SIZE = 20
COLOR_LIST = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
              (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
              (107, 127, 153), (174, 94, 97), (176, 192, 209)]


def draw_dots(turtle, number_of_dots):
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)

    for _ in range(number_of_dots):
        turtle.dot(DOT_SIZE, random.choice(COLOR_LIST))
        turtle.forward(50)

        if (_ + 1) % 10 == 0:
            turtle.setheading(90)
            turtle.forward(50)
            turtle.setheading(180)
            turtle.forward(500)
            turtle.setheading(0)


def main():
    turtle_module.colormode(255)
    turtle = turtle_module.Turtle()
    turtle.speed("fastest")
    turtle.penup()
    turtle.hideturtle()
    
    number_of_dots = 100
    draw_dots(turtle, number_of_dots)

    turtle_module.done()


if __name__ == '__main__':
    main()
