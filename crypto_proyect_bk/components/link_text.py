import reflex as rx

def link_text(text: str, url: str) -> rx.Component:
    return rx.link(
        text,
        href=url,
        #is_external = True,
        margin = "1%",
        size = "4"
    )