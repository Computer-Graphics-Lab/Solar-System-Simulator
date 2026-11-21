import turtle
import math
import random

# ==============================
# 1. CREATE GRAPHICS WINDOW
# ==============================

screen = turtle.Screen()
screen.title("Solar System Simulator")
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(0)

# ==============================
# 2. BACKGROUND STARS
# ==============================

stars = turtle.Turtle()
stars.speed(0)
stars.color("white")
stars.penup()
stars.hideturtle()

for i in range(150):

    x = random.randint(-480, 480)
    y = random.randint(-380, 380)

    stars.goto(x, y)
    stars.dot(random.randint(1, 3))

# ==============================
# 3. CREATE SUN
# ==============================

sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(2.5)
sun.penup()
sun.goto(0, 0)

# ==============================
# 4. PLANET INFORMATION
# ==============================

planets_data = [
    ("Mercury", "gray", 0.5, 80, 4.7),
    ("Venus", "orange", 0.8, 120, 3.5),
    ("Earth", "blue", 0.9, 165, 3.0),
    ("Mars", "red", 0.7, 210, 2.4),
    ("Jupiter", "brown", 1.8, 270, 1.3),
    ("Saturn", "gold", 1.5, 330, 0.9),
    ("Uranus", "light blue", 1.2, 380, 0.6),
    ("Neptune", "cyan", 1.2, 430, 0.4)
]

# ==============================
# 5. CREATE PLANETS
# ==============================

planets = []

for name, color, size, distance, speed in planets_data:

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

    # Create planet
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.shapesize(size)
    planet.penup()
    planet.goto(distance, 0)

    # Create planet label
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

# ==============================
# 6. DRAW ORBITAL PATHS
# ==============================

for name, color, size, distance, speed in planets_data:

    orbit = turtle.Turtle()
    orbit.speed(0)
    orbit.color("dim gray")
    orbit.pensize(1)
    orbit.penup()
    orbit.goto(0, -distance)
    orbit.pendown()
    orbit.circle(distance)
    orbit.hideturtle()

# ==============================
# 7. PLANETARY ANIMATION
# ==============================

running = True


def close_window():
    global running
    running = False
    screen.bye()


screen.getcanvas().winfo_toplevel().protocol(
    "WM_DELETE_WINDOW", close_window
)


# ==============================
# DRAW SATURN'S RING
# ==============================

def draw_ring(ring, x, y, start_angle, end_angle):

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


# ==============================
# PLANETARY ANIMATION FUNCTION
# ==============================

def animate():

    if not running:
        return

    saturn_position = None
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

            saturn_position = (x, y)
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
    # THIRD: Draw Saturn's two ring arcs
    # --------------------------------

    if saturn_position is not None:

        x, y = saturn_position

        # Upper half (behind Saturn)
        draw_ring(
            saturn["back_ring"],
            x, y,
            0, 180
        )

        # Lower half (in front of Saturn)
        draw_ring(
            saturn["front_ring"],
            x, y,
            180, 360
        )

    # --------------------------------
    # FOURTH: Update screen
    # --------------------------------

    screen.update()

    # --------------------------------
    # FIFTH: Control Saturn's ring layers
    # --------------------------------

    if saturn is not None:

        canvas = screen.getcanvas()

        # Keep the back ring behind Saturn
        for item in saturn["back_ring"].items:
            canvas.tag_lower(item)

        # Bring the front ring above everything
        for item in saturn["front_ring"].items:
            canvas.tag_raise(item)

    # --------------------------------
    # SIXTH: Schedule next animation
    # --------------------------------

    if running:
        screen.ontimer(animate, 20)


# ==============================
# 8. START SIMULATION
# ==============================

animate()

screen.mainloop()
