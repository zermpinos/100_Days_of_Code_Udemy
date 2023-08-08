import turtle

# Constants
PADDLE_SPEED = 50
PADDLE_SIZE = 5
BALL_SPEED = 1
BRICK_ROWS = 5
BRICK_COLUMNS = 10
BRICK_WIDTH = 50
BRICK_HEIGHT = 20

# Initial score
score = 0

# Set up the screen
window = turtle.Screen()
window.title("Breakout Clone")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Display score
turtle.write(f'Score: {score}', align="center", font=('Courier', 24, 'normal'))

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("green")
paddle.shapesize(stretch_wid=1, stretch_len=PADDLE_SIZE)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = BALL_SPEED
ball.dy = BALL_SPEED


# Function to create a brick
def create_brick(x, y):
    new_brick = turtle.Turtle()
    new_brick.shape("square")
    new_brick.color("black", "white")
    new_brick.penup()
    new_brick.goto(x, y)
    return new_brick


# Create bricks
bricks = [create_brick(-230 + col * BRICK_WIDTH, 180 - row * BRICK_HEIGHT)
          for row in range(BRICK_ROWS) for col in range(BRICK_COLUMNS)]


# Functions to move the paddle
def move_left():
    x = paddle.xcor() - PADDLE_SPEED
    paddle.setx(max(x, -290))  # Prevent paddle from going off-screen


def move_right():
    x = paddle.xcor() + PADDLE_SPEED
    paddle.setx(min(x, 290))  # Prevent paddle from going off-screen


# Keyboard bindings
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# Game state
game_is_on = True

# Main game loop
while game_is_on:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collisions
    if abs(ball.xcor()) > 290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        game_is_on = False  # End the game

    # Paddle collision
    if ball.dy < 0 and abs(ball.ycor() + 240) < 10 and abs(ball.xcor() - paddle.xcor()) < 50:
        ball.dy *= -1

    # Brick collisions
    for brick in bricks:
        if abs(ball.xcor() - brick.xcor()) < BRICK_WIDTH / 2 and abs(ball.ycor() - brick.ycor()) < BRICK_HEIGHT / 2:
            ball.dy *= -1
            score += 1
            brick.goto(-1000, -1000)  # Move the brick out of sight

    # Check if all bricks are destroyed
    if all(brick.ycor() == -1000 for brick in bricks):
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0
        ball.color("green")
        ball.write("YOU WIN!", align="center", font=("Courier", 24, "normal"))
        game_is_on = False  # End the game
