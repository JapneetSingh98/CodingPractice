import turtle
import functools

wn = turtle.Screen()
wn.title("Pong by @JapneetSingh98")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

def create_paddle(x_pos):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.color("white")
    paddle.penup()
    paddle.goto(x_pos, 0)
    paddle.score = 0
    return paddle

def create_ball():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.65
    ball.dy = 0.65
    return ball

def create_scoreboard():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0, Player B: 0", align="center", font=("Courier", 24, "normal"))
    return pen

def update_scoreboard(scoreboard, paddleA, paddleB):
    scoreboard.clear()
    scoreboard.write("Player A: {}, Player B: {}".format(paddleA.score, paddleB.score),
                     align="center", font=("Courier", 24, "normal"))

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

def check_left_right_border(ball, paddleA, paddleB, scoreboard):
    if ball.xcor() > 390:
        paddle = paddleA
    elif ball.xcor() < -390:
        paddle = paddleB
    else:
        return
    ball.goto(0, 0)
    ball.dx *= -1
    paddle.score += 1
    update_scoreboard(scoreboard, paddleA, paddleB)

def check_paddle_bounce(ball, paddleA, paddleB):
   if ball.xcor() > 330 and ball.xcor() < 340:
       paddle = paddleB
   elif ball.xcor() < -330 and ball.xcor() > -340:
       paddle = paddleA
   else:
       return
   upper = paddle.ycor() + 60
   lower = paddle.ycor() - 60
   if ball.ycor() < upper and ball.ycor() >= paddle.ycor():
       ball.dx *= -1
       ball.dy = abs(ball.dy)
   elif ball.ycor() < paddle.ycor() and ball.ycor() > lower:
       ball.dx *= -1
       ball.dy = 0 -abs(ball.dy)

paddleA = create_paddle(-350)
paddleB = create_paddle(350)
ball = create_ball()
scoreboard = create_scoreboard()

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
    check_left_right_border(ball, paddleA, paddleB, scoreboard)
    check_paddle_bounce(ball, paddleA, paddleB)