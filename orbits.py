import turtle
import math

from config import PLANETS_DATA


def create_orbits():
    """Draw the orbital paths of all eight planets."""

    orbits = []

    for name, color, size, distance, speed in PLANETS_DATA:

        orbit = turtle.Turtle()
        orbit.speed(0)
        orbit.color("dim gray")
        orbit.pensize(1)
        orbit.penup()
        orbit.goto(0, -distance)
        orbit.pendown()
        orbit.circle(distance)
        orbit.hideturtle()

        orbits.append(orbit)

    return orbits


def draw_ring(ring, x, y, start_angle, end_angle):
    """Draw a portion of Saturn's elliptical ring."""

    ring.clear()
    ring.penup()

    ring_x = 22
    ring_y = 9

    for angle in range(start_angle, end_angle + 1):

        px = x + ring_x * math.cos(math.radians(angle))
        py = y + ring_y * math.sin(math.radians(angle))

        if angle == start_angle:
            ring.goto(px, py)
            ring.pendown()
        else:
            ring.goto(px, py)

    ring.penup()


def draw_saturn_rings(saturn):
    """Draw Saturn's back and front ring arcs."""

    if saturn is None:
        return

    x, y = saturn["position"]

    # Upper half: behind Saturn
    draw_ring(
        saturn["back_ring"],
        x, y,
        0, 180
    )

    # Lower half: in front of Saturn
    draw_ring(
        saturn["front_ring"],
        x, y,
        180, 360
    )


def update_ring_layers(screen, saturn):
    """Maintain Saturn's front and back ring layering."""

    if saturn is None:
        return

    canvas = screen.getcanvas()

    # Keep the back ring behind Saturn
    for item in saturn["back_ring"].items:
        canvas.tag_lower(item)

    # Bring the front ring above everything
    for item in saturn["front_ring"].items:
        canvas.tag_raise(item)