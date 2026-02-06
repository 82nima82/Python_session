from turtle import Turtle , Screen
from snake import Snake
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(600 , 600)
screen.title("snake game")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game = True
while game :
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.exitonclick()