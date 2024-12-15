import reflex as rx
from crypto_proyect.misc.constants import crypto_methods as values
from crypto_proyect.logic.decrypt import methods

class FormState(rx.State):
    value: str = values[0]
    rsa_n: str = ""
    rsa_private_key: str = ""
    permutation_m: str = ""

    @rx.event
    def change_value(self, value: str):
        self.value = value

    @rx.event
    def change_rsa_n(self, rsa_n: str):
        self.rsa_n = rsa_n

    @rx.event
    def change_rsa_private_key(self, rsa_private_key: str):
        self.rsa_private_key = rsa_private_key

    @rx.event
    def change_permutation_m(self, permutation_m: str):
        self.permutation_m = permutation_m

class TextAreaState(rx.State):
    text: str = ""

    @rx.event
    def change_text(self, text: str):
        self.text = text

class CryptoProcess(rx.State):
    is_loading = False
    possible_values = ""
    most_english_word = ""

    @rx.event
    def process_text(self, method: str, pre_text: str, n: str = "", private_key: str = "", m: str = ""):
        if "".join(pre_text.split()) != "":
            self.is_loading = True
            try:
                if method == "RSA" and (not n or not private_key):
                    self.possible_values = "Ingrese tanto n como la clave privada"
                if method == "Permutación" and (not m or not m.isdigit()):
                    self.possible_values = "Ingrese un número entero para m"
                    return

                if method == "RSA":
                    self.possible_values = methods[method](pre_text, n, private_key)
                    self.most_english_word = self.possible_values
                elif method == "Permutacion":
                    self.possible_values = " ".join([x[0] + " (" + "-".join(x[1:]) + ") || " for x in methods[method](pre_text, int(m))[0]])
                    self.most_english_word = methods[method](pre_text, int(m))[1] 
                
                else:
                    self.possible_values = " ".join([x[0] + " (" + "-".join(x[1:]) + ") || " for x in methods[method](pre_text)[0]])
                    self.most_english_word = methods[method](pre_text)[1] 
                    
            except Exception as e:
                self.possible_values = f"Error: {str(e)}"
            
            finally:
                self.is_loading = False
        else:
            self.possible_values = ""

def decrypt_box() -> rx.Component:
    def method_specific_inputs():
        return rx.cond(
            FormState.value == "RSA",
            rx.vstack(
                rx.hstack(
                    rx.text("n: "),
                    rx.input(
                        placeholder="Ingrese n",
                        value=FormState.rsa_n,
                        on_change=FormState.change_rsa_n,
                        size="2"
                    )
                ),
                rx.hstack(
                    rx.text("Clave privada: "),
                    rx.input(
                        placeholder="Ingrese clave privada",
                        value=FormState.rsa_private_key,
                        on_change=FormState.change_rsa_private_key,
                        size="2"
                    )
                )
            ),
            rx.cond(
                FormState.value == "Permutacion",
                rx.vstack(
                    rx.hstack(
                        rx.text("Adivine el número de letras por cluster (m): "),
                        rx.input(
                            placeholder="Enter m",
                            value=FormState.permutation_m,
                            on_change=FormState.change_permutation_m,
                            size="2",
                            type="number"
                        )
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
                    method_specific_inputs(),
                    rx.button(
                        "Decrypt",
                        color_scheme="blue",
                        loading=CryptoProcess.is_loading,
                        disabled=CryptoProcess.is_loading,
                        on_click=CryptoProcess.process_text(
                            FormState.value, 
                            TextAreaState.text, 
                            FormState.rsa_n, 
                            FormState.rsa_private_key,
                            FormState.permutation_m
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
            rx.text(
                rx.text.strong("Opción más probable (inglés): "), 
                CryptoProcess.most_english_word
            ),
            loading=CryptoProcess.is_loading
        ),
        padding="2%",
        width="100%"
    )