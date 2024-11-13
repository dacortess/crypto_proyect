
import reflex as rx

from rxconfig import config

from crypto_proyect.views.navbar import navbar
from crypto_proyect.views.encrypt_box import encrypt_box
from crypto_proyect.views.decrypt_box import decrypt_box
from crypto_proyect.misc.constants import crypto_methods as values


class FormState(rx.State):
    value: str = values[0]

    @rx.event
    def change_value(self, value: str):
        self.value = value

class TextAreaState(rx.State):
    text: str = " "

    @rx.event
    def change_text(self, text: str):
        self.text = text


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            encrypt_box(),
            rx.spacer(),
            decrypt_box()
        )
    )

def code() -> rx.Component:
    return rx.box(
        navbar(),
    )

def about() -> rx.Component:
    return rx.box(
        navbar(),
    )

app = rx.App(

)

app.add_page(
    index,
    title = "Home | Crypto Analysis",
    description = "Project for Intro. to Cryptography class"
)

app.add_page(
    code,
    title = "Code | Crypto Analysis",
    description = "Project for Intro. to Cryptography class",
    route = "/code"
)

app.add_page(
    about,
    title = "About | Crypto Analysis",
    description = "Project for Intro. to Cryptography class",
    route = "/about"
)
