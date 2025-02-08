import reflex as rx
from link_bio.components.title import title

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran")
    )