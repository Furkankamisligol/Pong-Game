from turtle import Turtle, Screen
from ball import Ball
from pong_racket import Racket
from scoreboard import Scoreboard


pong_table = Screen()
pong_table.setup(width=800, height=600)
pong_table.title("Pong")
pong_table.bgcolor("black")
pong_table.tracer(0)
line_drawer = Turtle()
line_drawer.ht()
line_drawer.color("white")
line_drawer.pu()
line_drawer.goto(x=0, y=295)
line_drawer.seth(270)
for i in range(20):
    line_drawer.pd()
    line_drawer.fd(15)
    line_drawer.pu()
    line_drawer.fd(15)

Player_one = Racket((-350, 0))
Player_two = Racket((350, 0))

p_ball = Ball()

position_1 = (50, 230)
position_2 = (-50, 230)
score_1 = Scoreboard(position_1)
score_2 = Scoreboard(position_2)


pong_table.listen()
pong_table.onkey(fun=Player_one.move_up, key="w")
pong_table.onkey(fun=Player_one.move_down, key="s")
pong_table.onkey(fun=Player_two.move_up, key="Up")
pong_table.onkey(fun=Player_two.move_down, key="Down")

game_is_on = True

while game_is_on:
    pong_table.update()
    p_ball.move()
    if p_ball.ycor() > 280 or p_ball.ycor() < -280:
        k = p_ball.heading()
        new_k = 360-k
        p_ball.seth(new_k)
    if p_ball.xcor() > 340:
        if p_ball.distance(Player_two) <= 50:
            k = p_ball.heading()
            l = k % 90
            m = 90 - l
            n = k + 2*m
            p_ball.seth(n)

    elif p_ball.xcor() < -340:
        if p_ball.distance(Player_one) <= 50:
            k = p_ball.heading()
            l = k % 90
            m = 90 - l
            n = k + 2 * m
            p_ball.seth(n)
    if p_ball.xcor() > 400:
        score_1.clear()
        score_1.score += 1
        p_ball.start_angle()

    if p_ball.xcor() < -400:
        score_2.clear()
        score_2.score += 1
        p_ball.start_angle()
    score_1.write_score()
    score_2.write_score()

pong_table.exitonclick()
