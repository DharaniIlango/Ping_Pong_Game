"""Ping Pong Game using Python3
Author: #D_1209"""

#import required modules
import turtle

window =turtle.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Scoring
score_a = 0
score_b = 0

# Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(10)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)

# Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(10)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350,0)

# Ball Specifications
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = 0.200
ball.dy = -0.200

# Pen Specifications (Scoring)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 30, "normal"))

# Required Functions
def paddle_right_up():
    y=paddle_right.ycor()
    y+=20
    paddle_right.sety(y)
    
def paddle_right_down():
    y=paddle_right.ycor()
    y-=20
    paddle_right.sety(y)
    
def paddle_left_up():
    y=paddle_left.ycor()
    y+=20
    paddle_left.sety(y)
    
def paddle_left_down():
    y=paddle_left.ycor()
    y-=20
    paddle_left.sety(y)

# Binding the Keys
window.listen()
window.onkeypress(paddle_left_up, 'w')
window.onkeypress(paddle_left_down, 's')
window.onkeypress(paddle_right_up, 'Up')
window.onkeypress(paddle_right_down, 'Down')

#main game loop
while True:
    window.update()
    
    # Moving the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border limit
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 30, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 30, "normal"))
        
    # Paddle and Ball Contact
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1