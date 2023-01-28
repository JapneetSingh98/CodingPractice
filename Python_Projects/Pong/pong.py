import turtle
import functools

wn = turtle.Screen()
wn.title("Pong by @JapneetSingh98")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle
def create_paddle(x_pos):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.color("white")
    paddle.penup()
    paddle.goto(x_pos, 0)
    return paddle

def create_ball():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    return ball

def move_paddle(paddle, direction):
    y = paddle.ycor()
    if direction == "up":
        y += 20
    elif direction == "down":
        y -= 20
    # TODO limit the range in order to keep the paddle within the screen
    paddle.sety(y)

paddleA = create_paddle(-350)
paddleB = create_paddle(350)
ball = create_ball()

wn.listen()
wn.onkeypress(functools.partial(move_paddle, paddleA, "up"), "w")
wn.onkeypress(functools.partial(move_paddle, paddleA, "down"), "s")
wn.onkeypress(functools.partial(move_paddle, paddleB, "up"), "o")
wn.onkeypress(functools.partial(move_paddle, paddleB, "down"), "k")

# Main game loop
while True:
    wn.update()