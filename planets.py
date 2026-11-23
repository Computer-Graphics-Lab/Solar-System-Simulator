import turtle

from config import PLANETS_DATA


def create_sun():
    """Create the Sun at the center of the solar system."""

    sun = turtle.Turtle()
    sun.shape("circle")
    sun.color("yellow")
    sun.shapesize(2.5)
    sun.penup()
    sun.goto(0, 0)

    return sun


def create_planets():
    """Create all planets, their labels, and Saturn's rings."""

    planets = []

    for name, color, size, distance, speed in PLANETS_DATA:

        back_ring = None
        front_ring = None

        # Create Saturn's ring objects
        if name == "Saturn":

            back_ring = turtle.Turtle()
            back_ring.hideturtle()
            back_ring.speed(0)
            back_ring.color("wheat")
            back_ring.pensize(2)
            back_ring.penup()

            front_ring = turtle.Turtle()
            front_ring.hideturtle()
            front_ring.speed(0)
            front_ring.color("wheat")
            front_ring.pensize(2)
            front_ring.penup()

        # Create Planet
        planet = turtle.Turtle()
        planet.shape("circle")
        planet.color(color)
        planet.shapesize(size)
        planet.penup()
        planet.goto(distance, 0)

        # Create Planet label
        label = turtle.Turtle()
        label.hideturtle()
        label.penup()
        label.color("white")

        planets.append({
            "turtle": planet,
            "back_ring": back_ring,
            "front_ring": front_ring,
            "label": label,
            "name": name,
            "distance": distance,
            "angle": 0,
            "speed": speed
        })

    return planets