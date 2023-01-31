import turtle
import functools
from constants import *

wn = turtle.Screen()
wn.title("Pong by @JapneetSingh98")
wn.bgcolor("black")
wn.setup(width=PAGE_WIDTH, height=PAGE_HEIGHT)
wn.tracer(0)

def create_paddle(x_pos):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.shapesize(stretch_wid=PADDLE_HEIGHT/20, stretch_len=1)
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
    ball.dx = BALL_DX
    ball.dy = BALL_DY
    return ball

def create_scoreboard():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, PAGE_HEIGHT/2 - 40)
    pen.write("Player A: 0, Player B: 0", align="center", font=("Courier", 24, "normal"))
    return pen

def update_scoreboard(scoreboard, paddleA, paddleB):
    scoreboard.clear()
    scoreboard.write("Player A: {}, Player B: {}".format(paddleA.score, paddleB.score),
                     align="center", font=("Courier", 24, "normal"))

def move_paddle(paddle, direction):
    y = paddle.ycor()
    if direction == "up":
        y += PADDLE_MOVE
        # if y > PAGE_HEIGHT/2 - PADDLE_HEIGHT/2:
        #     y = PAGE_HEIGHT/2 - PADDLE_HEIGHT/2
    elif direction == "down":
        y -= PADDLE_MOVE
        # if y < PADDLE_HEIGHT/2 - PAGE_HEIGHT/2:
        #     y = PADDLE_HEIGHT/2 - PAGE_HEIGHT/2
    paddle.sety(y)

def check_top_bottom_border(ball):
    if ball.ycor() > PAGE_HEIGHT/2 - 10 or ball.ycor() < 10 - PAGE_HEIGHT/2:
        ball.dy *= -1

def check_left_right_border(ball, paddleA, paddleB, scoreboard):
    if ball.xcor() > PAGE_WIDTH/2 - 10:
        paddle = paddleA
    elif ball.xcor() < 10 - PAGE_WIDTH/2:
        paddle = paddleB
    else:
        return
    ball.goto(0, 0)
    ball.dx *= -1
    paddle.score += 1
    update_scoreboard(scoreboard, paddleA, paddleB)

def check_paddle_bounce(ball, paddleA, paddleB):
   if ball.xcor() > PAGE_WIDTH/2 - ENDZONE_WIDTH - 20 and ball.xcor() < PAGE_WIDTH/2 - ENDZONE_WIDTH - 10:
       paddle = paddleB
   elif ball.xcor() < ENDZONE_WIDTH + 20 - PAGE_WIDTH/2 and ball.xcor() > ENDZONE_WIDTH + 10 - PAGE_WIDTH/2:
       paddle = paddleA
   else:
       return
   upper = paddle.ycor() + PADDLE_HEIGHT/2 + 10
   lower = paddle.ycor() - PADDLE_HEIGHT/2 - 10
   if ball.ycor() < upper and ball.ycor() >= paddle.ycor():
       ball.dx *= -1
       ball.dy = abs(ball.dy)
   elif ball.ycor() < paddle.ycor() and ball.ycor() > lower:
       ball.dx *= -1
       ball.dy = 0 -abs(ball.dy)

paddleA = create_paddle(ENDZONE_WIDTH - PAGE_WIDTH/2)
paddleB = create_paddle(PAGE_WIDTH/2 - ENDZONE_WIDTH)
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