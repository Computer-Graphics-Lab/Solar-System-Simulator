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

# 1. CREATE GRAPHICS WINDOW
screen = turtle.Screen()
screen.title("Solar System Simulator")
screen.bgcolor(SCREEN_BACKGROUND)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

# 2. CREATE BACKGROUND
stars = create_background()

# 3. CREATE SUN
sun = create_sun()

# 4. CREATE PLANETS
planets = create_planets()

# Store original planetary angles
for planet in planets:
    planet["initial_angle"] = planet["angle"]

# 5. DRAW ORBITAL PATHS
orbits = create_orbits()

# 6. SIMULATION CONTROL
state = {
    "running": True,
    "timer_id": None,
    "delay": ANIMATION_DELAY,
    "generation": 0,
    "closed": False
}

def set_running(value):
    state["running"] = value

    if not value:
        state["closed"] = True

def cancel_animation():
    """Cancel the currently scheduled animation."""

    state["generation"] += 1

    timer_id = state["timer_id"]

    if timer_id is not None:
        try:
            screen.getcanvas().after_cancel(timer_id)
        except Exception:
            pass

    state["timer_id"] = None

def change_speed(action):
    """Control simulation speed, pause, resume and reset."""

    if state["closed"]:
        return

    if action == "toggle":

        if state["running"]:
            state["running"] = False
            cancel_animation()
            print("Simulation Paused")

        else:
            state["running"] = True
            print("Simulation Resumed")
            animate()

    elif action == "faster":

        state["delay"] = max(
            5,
            state["delay"] - 5
        )

        print("Simulation Speed Increased")

    elif action == "slower":

        state["delay"] = min(
            100,
            state["delay"] + 5
        )

        print("Simulation Speed Decreased")

    elif action == "reset":

        # Cancel previous animation
        cancel_animation()

        # Restore original planetary angles.
        # Subtract speed because animate() adds it
        # before calculating the next position.
        for planet in planets:
            planet["angle"] = (
                planet["initial_angle"] - planet["speed"]
            )

        # Restore original animation speed
        state["delay"] = ANIMATION_DELAY

        # Resume simulation
        state["running"] = True

        print("Simulation Reset")
        print(f"Animation delay: {state['delay']} ms")

        animate()
        return

    print(f"Animation delay: {state['delay']} ms")

# 7. SET UP KEYBOARD CONTROLS
setup_controls(
    screen,
    set_running,
    cancel_animation,
    change_speed
)

# 8. PLANETARY ANIMATION
def animate(generation=None):
    if not state["running"]:
        return

    try:
        if not screen.getcanvas().winfo_exists():
            return
    except Exception:
        return

    if generation is None:
        generation = state["generation"]

    # Prevent outdated callbacks
    if state["closed"]:
        return

    if not state["running"]:
        return

    if generation != state["generation"]:
        return

    # Current timer has executed
    state["timer_id"] = None

    saturn = None

    # FIRST: Calculate planet positions
    for planet in planets:

        planet["angle"] += planet["speed"]

        angle_rad = math.radians(planet["angle"])

        x = planet["distance"] * math.cos(angle_rad)
        y = planet["distance"] * math.sin(angle_rad)

        planet["position"] = (x, y)

        if planet["name"] == "Saturn":
            saturn = planet

    # SECOND: Move planets and labels
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

    # THIRD: Draw Saturn's ring arcs
    if saturn is not None:
        draw_saturn_rings(saturn)

    # FOURTH: Update screen
    screen.update()

    # FIFTH: Maintain Saturn's ring layers
    if saturn is not None:
        try:
            if screen.getcanvas().winfo_exists():
                update_ring_layers(screen, saturn)
        except turtle.Terminator:
            return
        except Exception:
            return
        update_ring_layers(screen, saturn)

    # SIXTH: Schedule next animation
    if (
        state["running"]
        and not state["closed"]
        and generation == state["generation"]
    ):

        state["timer_id"] = screen.ontimer(
            lambda g=generation: animate(g),
            state["delay"]
        )

# 9. START SIMULATION
animate()

screen.mainloop()