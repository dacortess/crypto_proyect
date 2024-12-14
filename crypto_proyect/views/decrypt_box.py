import reflex as rx
from crypto_proyect.misc.constants import crypto_methods as values
from crypto_proyect.logic.decrypt import methods

class FormState(rx.State):
    value: str = values[0]
    rsa_n: str = ""
    rsa_private_key: str = ""

    @rx.event
    def change_value(self, value: str):
        self.value = value

    @rx.event
    def change_rsa_n(self, rsa_n: str):
        self.rsa_n = rsa_n

    @rx.event
    def change_rsa_private_key(self, rsa_private_key: str):
        self.rsa_private_key = rsa_private_key

class TextAreaState(rx.State):
    text: str = ""

    @rx.event
    def change_text(self, text: str):
        self.text = text

class CryptoProcess(rx.State):
    is_loading = False
    possible_values = ""

    @rx.event
    def process_text(self, method: str, pre_text: str, n: str = "", private_key: str = ""):
        if "".join(pre_text.split()) != "":
            self.is_loading = True
            try:
                if method == "RSA" and (not n or not private_key):
                    self.possible_values = "Please provide both n and private key for RSA decryption"
                    return

                if method == "RSA":
                    self.possible_values = methods[method](pre_text, n, private_key)
                else:
                    self.possible_values = " ".join([x[0] + " (" + "-".join(x[1:]) + ") || " for x in methods[method](pre_text)])
            except Exception as e:
                self.possible_values = f"Error: {str(e)}"
            finally:
                self.is_loading = False
        else:
            self.possible_values = ""

def decrypt_box() -> rx.Component:
    def rsa_inputs():
        return rx.cond(
            FormState.value == "RSA",
            rx.vstack(
                rx.hstack(
                    rx.text("n: "),
                    rx.input(
                        placeholder="Enter n",
                        value=FormState.rsa_n,
                        on_change=FormState.change_rsa_n,
                        size="2"
                    )
                ),
                rx.hstack(
                    rx.text("Private Key: "),
                    rx.input(
                        placeholder="Enter private key",
                        value=FormState.rsa_private_key,
                        on_change=FormState.change_rsa_private_key,
                        size="2"
                    )
                )
            )
        )

    return rx.vstack(
        rx.heading(
            "Decrypt Message", 
            size="5"
        ),
        rx.spacer(),
        rx.flex(
            rx.hstack(
                rx.text_area(
                    placeholder="Type here...",
                    text=TextAreaState.text,
                    on_change=TextAreaState.change_text,
                    size="3",
                    variant="surface",
                    resize="both",
                    min_length=1,
                ),
                rx.spacer(),
                rx.vstack(
                    rx.hstack(
                        rx.text("Metodo:"),
                        rx.center(
                            rx.select(
                                values,
                                value=FormState.value,
                                on_change=FormState.change_value
                            )
                        )
                    ),
                    rsa_inputs(),
                    rx.button(
                        "Decrypt",
                        color_scheme="blue",
                        loading=CryptoProcess.is_loading,
                        disabled=CryptoProcess.is_loading,
                        on_click=CryptoProcess.process_text(
                            FormState.value, 
                            TextAreaState.text, 
                            FormState.rsa_n, 
                            FormState.rsa_private_key
                        )
                    )
                ),
            ),
            style={
                "flex-direction": ["column", "row"],
                "width": "100%",
            },
        ),
        rx.skeleton(
            rx.text(
                rx.text.strong("Possible Decrypted Texts: "), 
                CryptoProcess.possible_values
            ),
            loading=CryptoProcess.is_loading
        ),
        padding="2%",
        width="100%"
    )