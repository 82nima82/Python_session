from turtle import Turtle , Screen
import random
A_turtle = Turtle()
A_turtle.shape("turtle")
A_turtle.color("blue","cyan")
# A_turtle.forward(200)
# A_turtle.right(90)
# A_turtle.forward(200)
# A_turtle.right(90)
# A_turtle.forward(200)
# A_turtle.right(90)
# A_turtle.forward(200)
# A_turtle.right(90)
# for _ in range(10):
#     A_turtle.forward(10)
#     A_turtle.color("white")
#     A_turtle.forward(10)
#     A_turtle.color("blue","cyan")
# for _ in range(3):
#     A_turtle.forward(50)
#     A_turtle.right(120)
# A_turtle.color("green")
# for _ in range(4):
#     A_turtle.forward(50)
#     A_turtle.right(90)
# A_turtle.color("gray")
# for _ in range(5):
#     A_turtle.forward(50)
#     A_turtle.right(72)
# A_turtle.color("orange")
# for _ in range(6):
#     A_turtle.forward(50)
#     A_turtle.right(60)
# A_turtle.color("black")
# for _ in range(7):
#     A_turtle.forward(50)
#     A_turtle.right(51)
# A_turtle.color("red")
# for _ in range(8):
#     A_turtle.forward(50)
#     A_turtle.right(45)
color = ["blue","cyan","green","gray","black","orange","red"]
y = [1,2,3,4]
for i in range(100):
    a = random.choice(y)
    b = random.choice(color)
    if a == 1 :
        A_turtle.color(b)
        A_turtle.right(90)
        A_turtle.forward(20)
    if a == 2:
        A_turtle.color(b)
        A_turtle.right(180)
        A_turtle.forward(20)
    if a == 3:
        A_turtle.color(b)
        A_turtle.right(270)
        A_turtle.forward(20)
    if a == 4:
        A_turtle.color(b)
        A_turtle.right(360)
        A_turtle.forward(20)
B = Screen()
B.exitonclick()