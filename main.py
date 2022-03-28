# let us begin with pong game

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.title("PONG GAME welcome")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
score = Scoreboard()

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
speed = 0.060
game_is_on = True
while game_is_on:
    time.sleep(speed)
    ball.ball_movement()
    screen.update()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if speed > 0.005:
            speed -= 0.005


# score for  right paddle
    if ball.xcor() < -400:
        ball.score_for_paddle()
        speed = 0.060
        score.right_paddle_score()
        screen.update()
        time.sleep(1)

# score for left paddle
    if ball.xcor() > 400:
        ball.score_for_paddle()
        speed = 0.060
        score.left_paddle_score()
        screen.update()
        time.sleep(1)














screen.exitonclick()

