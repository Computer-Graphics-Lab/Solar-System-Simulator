def setup_controls(screen, set_running, cancel_animation):
    """Configure window closing behavior."""

    def close_window():
        set_running(False)

        cancel_animation()

        screen.bye()

    screen.getcanvas().winfo_toplevel().protocol(
        "WM_DELETE_WINDOW",
        close_window
    )