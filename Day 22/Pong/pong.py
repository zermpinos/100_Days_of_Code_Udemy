import time
from turtle import Screen, Turtle


class Ball(Turtle):
    """
    Ball class represents the ball in the Pong game.
    Inherits from the Turtle class.
    """

    def __init__(self):
        super().__init__()
        self.color("white")  # Set ball color to white
        self.shape("circle")
        self.penup()
        self.x_move = 4
        self.y_move = 4
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()


class Paddle(Turtle):
    """
    Paddle class represents a paddle in the Pong game.
    Inherits from the Turtle class.
    """

    def __init__(self, position):
        super().__init__()
        self.color("white")  # Set paddle color to white
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class Scoreboard(Turtle):
    """
    Scoreboard class represents the scoreboard in the Pong game.
    Inherits from the Turtle class.
    """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.winner = None
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        if self.l_score >= 3:
            self.winner = "Left player"
            self.game_over()
        else:
            self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        if self.r_score >= 3:
            self.winner = "Right player"
            self.game_over()
        else:
            self.update_scoreboard()

    def game_over(self):
        self.update_scoreboard()
        time.sleep(1)  # Pause for a moment before showing the winner message
        self.clear()
        self.goto(0, 0)
        self.write("Game Over! {} wins!".format(self.winner), align="center", font=("Arial", 36, "normal"))


def setup_screen():
    """
    Sets up the game screen with a black background, 800x600 size,
    Pong title, and no tracer.
    Returns the created screen.
    """
    screen = Screen()
    screen.bgcolor("black")  # Set background color to black
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)
    return screen


def setup_game_elements():
    """
    Creates the game elements: paddles, ball, and scoreboard.
    Returns the created paddles, ball, and scoreboard.
    """
    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()
    return r_paddle, l_paddle, ball, scoreboard


def setup_controls(screen, r_paddle, l_paddle):
    """
    Sets up the controls for the game, binding the paddle movements
    to the corresponding keys.
    """
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")


def main():
    screen = setup_screen()
    r_paddle, l_paddle, ball, scoreboard = setup_game_elements()
    setup_controls(screen, r_paddle, l_paddle)

    game_is_on = True

    def exit_game():
        nonlocal game_is_on
        game_is_on = False

    screen.onkeypress(exit_game, "Escape")
    screen.listen()

    while game_is_on:
        screen.update()
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddle
        if (
            ball.distance(r_paddle) < 50 and ball.xcor() > 320
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320
        ):
            ball.bounce_x()

        # Detect R paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        # Detect L paddle misses:
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

        if scoreboard.winner:
            game_is_on = False  # End the game when a winner is determined

        time.sleep(ball.move_speed)  # Move this line to the end of the loop

    screen.mainloop()


main()
