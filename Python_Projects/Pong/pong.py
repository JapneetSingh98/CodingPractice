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
    ball.dx = 0.5
    ball.dy = 0.5
    return ball

def move_paddle(paddle, direction):
    y = paddle.ycor()
    if direction == "up":
        y += 20
    elif direction == "down":
        y -= 20
    # TODO limit the range in order to keep the paddle within the screen
    paddle.sety(y)

def check_top_bottom_border(ball):
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

def check_left_right_border(ball):
    # Ball goes past paddles
    # TODO add scoring
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

def check_paddle_bounce(ball, paddleA, paddleB):
   if ball.xcor() > 330 and ball.xcor() < 340:
       upper = paddleB.ycor() + 60
       lower = paddleB.ycor() - 60
       if ball.ycor() < upper and ball.ycor() > lower:
           ball.dx *= -1
   elif ball.xcor() < -330 and ball.xcor() > -340:
       upper = paddleA.ycor() + 60
       lower = paddleA.ycor() - 60
       if ball.ycor() < upper and ball.ycor() > lower:
           ball.dx *= -1

paddleA = create_paddle(-350)
paddleB = create_paddle(350)
ball = create_ball()


wn.listen()
wn.onkeypress(functools.partial(move_paddle, paddleA, "up"), "w")
wn.onkeypress(functools.partial(move_paddle, paddleA, "down"), "s")
wn.onkeypress(functools.partial(move_paddle, paddleB, "up"), "p")
wn.onkeypress(functools.partial(move_paddle, paddleB, "down"), "l")

# Main game loop
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    check_top_bottom_border(ball)
    check_left_right_border(ball)
    check_paddle_bounce(ball, paddleA, paddleB)