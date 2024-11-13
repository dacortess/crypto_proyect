import reflex as rx
from crypto_proyect.components.link_text import link_text

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            #rx.image(),
            rx.heading(
                "Crypto Analysis",
                size = "6",
                margin = "1%"
                ),
            rx.spacer(),
            link_text(
                "Home",
                "/"
                ),
            link_text(
                "Code",
                "/code"
                ),
            link_text(
                "About",
                "/about"
                ),
            width = "100%",
        ),
        position = "sticky",
        border_bottom = "0.25em solid",
        z_index="999",
        top = "0",
        padding = "1%",
        width = "100%",
        bg = "black"
    )