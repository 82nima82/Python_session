from turtle import Screen
from paddle import paddle
screen = Screen()
screen.setup(800 , 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_paddle = paddle((350 , 0))
l_paddle = paddle((-350 , 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
while game_is_on :
    screen.update()
screen.exitonclick()