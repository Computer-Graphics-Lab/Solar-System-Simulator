import turtle
import random

from config import STAR_COUNT


def create_background():
    """Create the space background with randomly positioned stars."""

    stars = turtle.Turtle()
    stars.speed(0)
    stars.color("white")
    stars.penup()
    stars.hideturtle()

    for i in range(STAR_COUNT):

        x = random.randint(-480, 480)
        y = random.randint(-380, 380)

        stars.goto(x, y)
        stars.dot(random.randint(1, 3))

    return stars