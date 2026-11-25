import turtle
import random

from config import (
    STAR_COUNT,
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

def create_background():
    """Create the space background with randomly positioned stars."""

    stars = turtle.Turtle()
    stars.speed(0)
    stars.penup()
    stars.hideturtle()

    for _ in range(STAR_COUNT):

        x = random.randint(
            -SCREEN_WIDTH // 2 + 10,
            SCREEN_WIDTH // 2 - 10
        )

        y = random.randint(
            -SCREEN_HEIGHT // 2 + 10,
            SCREEN_HEIGHT // 2 - 10
        )

        star_size = random.choice([1, 2, 2, 3])

        star_color = random.choice([
            "white",
            "light gray",
            "light blue"
        ])

        stars.goto(x, y)
        stars.color(star_color)
        stars.dot(star_size)

    return stars