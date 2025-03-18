from turtle import Screen, Turtle
from bar import Bar
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong")
screen.tracer(0)


right_bar= Bar((350,0))
left_bar= Bar((-350,0))
ball= Ball()
score= Scoreboard()


screen.listen()
screen.onkey(key="o",fun=right_bar.up)
screen.onkey(key="l",fun=right_bar.down)

screen.onkey(key="w",fun=left_bar.up)
screen.onkey(key="s",fun=left_bar.down)


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(right_bar) <50 and ball.xcor() >320 or ball.distance(left_bar) <50 and ball.xcor() < -320:
        ball.collide()

    if ball.xcor() > 380:
        ball.come_middle()
        score.l_point()

    if ball.xcor() < -380:
        ball.come_middle()
        score.r_point()


screen.exitonclick()