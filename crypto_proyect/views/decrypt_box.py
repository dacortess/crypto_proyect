import reflex as rx
from crypto_proyect.misc.constants import crypto_methods as values
from crypto_proyect.logic.decrypt import methods

class FormState(rx.State):
    value: str = values[0]

    @rx.event
    def change_value(self, value: str):
        self.value = value

class TextAreaState(rx.State):
    text: str = ""

    @rx.event
    def change_text(self, text: str):
        self.text = text

class CryptoProcess(rx.State):
    is_loading = False
    possible_values = ""

    @rx.event
    def process_text(self, method: str, pre_text: str):
        if "".join(pre_text.split()) != "":
            self.is_loading = True
            try:
                self.possible_values = " ".join([x[0] + " (" + "-".join(x[1:]) + ") || " for x in methods[method](pre_text)])
            except Exception as e:
                raise(e)
            finally:
                self.is_loading = False
        else:
            self.possible_values = ""

def decrypt_box() -> rx.Component:
    return rx.vstack(
        #rx.text(f"{FormState.value} {TextAreaState.text}"), # Debug
        rx.heading(
            f"Decrypt Message", 
            size = "5"
            ),
            rx.spacer(),
        rx.flex(
            rx.hstack(
                rx.text_area(
                    placeholder = "Type here...",
                    text = TextAreaState.text,
                    on_change = TextAreaState.change_text,
                    size = "3",
                    variant = "surface",
                    resize = "both",
                    min_legth = 1,

                ),
                rx.spacer(),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Metodo:"
                        ),
                        rx.center(
                            rx.select(
                                values,
                                value = FormState.value,
                                on_change = FormState.change_value
                            )
                        )
                    ),
                    rx.button(
                        "Decrypt",
                        color_scheme = "blue",
                        loading = CryptoProcess.is_loading,
                        disabled = CryptoProcess.is_loading,
                        on_click = CryptoProcess.process_text(FormState.value, TextAreaState.text)
                    )
                ),
            ),
            style={
                "flex-direction": ["column", "row"],  # Cambia a "row" en pantallas grandes
                "width": "100%",                      # Para que ocupe todo el ancho
            },
        ),
        rx.skeleton(
            rx.text(
                rx.text.strong("Possible Decrypted Texts: "), 
                CryptoProcess.possible_values
            ),
            loading = CryptoProcess.is_loading
        ),
        padding = "2%",
        width = "100%"
    ) 