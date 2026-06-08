import turtle
from turtle import Turtle, Screen
import random


turtle1 = Turtle()
turtle1.shape("circle")
turtle1.speed(1)
colors = ["tomato", "forest green", "medium slate blue", "pale goldenrod", "dodger blue", "orange", "dark goldenrod", "rosy brown"]
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# todo Ex: 2
# for _ in range(4):
#     turtle1.forward(10)
#     turtle1.penup()
#     turtle1.forward(10)
#     turtle1.pendown()

# todo Ex: 3
# for i in range(3,9):
#     angle = 360/i
#     turtle1.color(random.choice(colors))
#     for _ in range(i):
#         turtle1.right(angle)
#         turtle1.forward(100)

# Todo Ex:4
# distance = [turtle1.forward, turtle1.backward]
# movement = [turtle1.left, turtle1.right]
# angle = [90, 0]
# turtle1.pen(pensize=10)
# while True:
#     turtle1.color(random_color())
#     random.choice(movement)(random.choice(angle))
#     random.choice(distance)(60)


# Todo Ex:5
turtle1.speed(25)
def draw_spiral(gap_size):
    for _ in range(int(360/gap_size)):
        turtle1.color(random_color())
        turtle1.circle(100)
        turtle1.left(gap_size)

draw_spiral(5)


screen = Screen()
screen.exitonclick()
