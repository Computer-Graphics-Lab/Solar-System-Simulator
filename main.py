import turtle
import math

# Import project modules
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_BACKGROUND,
    ANIMATION_DELAY
)

from background import create_background
from planets import create_sun, create_planets
from orbits import (
    create_orbits,
    draw_saturn_rings,
    update_ring_layers
)
from controls import setup_controls


# ==============================
# 1. CREATE GRAPHICS WINDOW
# ==============================

screen = turtle.Screen()
screen.title("Solar System Simulator")
screen.bgcolor(SCREEN_BACKGROUND)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)


# ==============================
# 2. CREATE BACKGROUND
# ==============================

stars = create_background()


# ==============================
# 3. CREATE SUN
# ==============================

sun = create_sun()


# ==============================
# 4. CREATE PLANETS
# ==============================

planets = create_planets()


# ==============================
# 5. DRAW ORBITAL PATHS
# ==============================

orbits = create_orbits()


# ==============================
# 6. SIMULATION CONTROL
# ==============================

state = {
    "running": True,
    "timer_id": None
}


def set_running(value):
    state["running"] = value


def cancel_animation():
    timer_id = state["timer_id"]

    if timer_id is not None:
        try:
            screen.getcanvas().after_cancel(timer_id)
        except turtle.TurtleGraphicsError:
            pass
        except Exception:
            pass

        state["timer_id"] = None


setup_controls(screen, set_running, cancel_animation)


# ==============================
# 7. PLANETARY ANIMATION
# ==============================

def animate():

    if not state["running"]:
        return

    saturn = None

    # --------------------------------
    # FIRST: Calculate planet positions
    # --------------------------------

    for planet in planets:

        planet["angle"] += planet["speed"]

        angle_rad = math.radians(planet["angle"])

        x = planet["distance"] * math.cos(angle_rad)
        y = planet["distance"] * math.sin(angle_rad)

        planet["position"] = (x, y)

        if planet["name"] == "Saturn":
            saturn = planet

    # --------------------------------
    # SECOND: Move planets and labels
    # --------------------------------

    for planet in planets:

        x, y = planet["position"]

        planet["turtle"].goto(x, y)

        planet["label"].clear()
        planet["label"].goto(x + 12, y + 12)

        planet["label"].write(
            planet["name"],
            align="left",
            font=("Arial", 8, "normal")
        )

    # --------------------------------
    # THIRD: Draw Saturn's ring arcs
    # --------------------------------

    if saturn is not None:
        draw_saturn_rings(saturn)

    # --------------------------------
    # FOURTH: Update screen
    # --------------------------------

    screen.update()

    # --------------------------------
    # FIFTH: Maintain Saturn's ring layers
    # --------------------------------

    if saturn is not None:
        update_ring_layers(screen, saturn)

    # --------------------------------
    # SIXTH: Schedule next animation
    # --------------------------------

    if state["running"]:
        state["timer_id"] = screen.ontimer(
            animate,
            ANIMATION_DELAY
        )


# ==============================
# 8. START SIMULATION
# ==============================

animate()

screen.mainloop()