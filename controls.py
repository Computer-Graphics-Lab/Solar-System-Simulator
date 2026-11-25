import turtle

def setup_controls(screen, set_running, cancel_animation, change_speed):
    """Configure keyboard controls and window closing behavior."""

    def toggle_simulation():
        change_speed("toggle")

    def close_window():
        set_running(False)
        cancel_animation()

        try:
            screen.bye()
        except turtle.Terminator:
            pass

    screen.listen()

    screen.onkey(toggle_simulation, "space")
    screen.onkey(close_window, "Escape")
    screen.onkey(lambda: change_speed("faster"), "plus")
    screen.onkey(lambda: change_speed("slower"), "minus")
    screen.onkey(lambda: change_speed("reset"), "r")

    screen.getcanvas().winfo_toplevel().protocol(
        "WM_DELETE_WINDOW",
        close_window
    )
