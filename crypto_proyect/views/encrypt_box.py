import reflex as rx
from crypto_proyect.misc.constants import crypto_methods as values
from crypto_proyect.misc.constants import crypto_methods_info as values_info
from crypto_proyect.logic.encrypt import methods

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
    processed_text = ""
    possible_keys = ""

    @rx.event
    def process_text(self, method: str, pre_text: str, params):
        self.is_loading = True
        if "".join(pre_text.split()) != "":
            try:
                if method == "Permutacion":
                    self.processed_text, self.possible_keys = methods[method](pre_text.replace(" ", ""), *(int(params[0]), params[1]))
                else:
                    processed_params = (int(params[0]), int(params[1]) if params[1].isdigit() else 1)
                    self.processed_text, self.possible_keys = methods[method](pre_text.replace(" ", ""), *processed_params)
            except Exception as e:
                raise(e)
                self.processed_text = f"Error: {str(e)}"
                self.possible_keys = ""
            finally:
                self.is_loading = False
        else:
            self.processed_text = ""
            self.possible_keys = ""

class ParamState(rx.State):
    value1: str = "1"
    value2: str = "1"

    @rx.event
    def change_value1(self, value1: str):
        self.value1 = value1
    
    @rx.event
    def change_value2(self, value2: str):
        self.value2 = value2

    @rx.event
    def reset_params(self):
        self.value1 = "1"
        self.value2 = "1"

def encrypt_box() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Encrypt Message", 
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
                                on_change=[
                                    FormState.change_value,
                                    ParamState.reset_params  # Reset params when method changes
                                ]
                            )
                        )
                    ),
                    parameters(),
                ),
                rx.spacer(),
                rx.button(
                    "Encrypt",
                    color_scheme="blue",
                    loading=CryptoProcess.is_loading,
                    on_click=CryptoProcess.process_text(FormState.value, TextAreaState.text, (ParamState.value1, ParamState.value2))
                ),
            ),
            style={
                "flex-direction": ["column", "row"],
                "width": "100%",
            },
        ),
        rx.skeleton(
            rx.text(
                rx.text.strong("Encrypted Text: "), 
                CryptoProcess.processed_text,
            ),
            rx.text(
                rx.text.strong("Key: "), 
                CryptoProcess.possible_keys,
            ),
            loading=CryptoProcess.is_loading
        ),
        padding="2%",
        width="100%"
    ) 

def parameters() -> rx.Component:
    return rx.hstack(
        rx.cond(
            FormState.value == "Desplazamiento",
            rx.hstack(
                rx.text("Parametros: "),
                rx.center(
                    rx.select(
                        values_info["Desplazamiento"]["range"],
                        value1=ParamState.value1,
                        on_change=ParamState.change_value1
                    ),
                ),
            )
        ),
        rx.cond(
            FormState.value == "Afin",
            rx.hstack(
                rx.text("Parametros: "),
                rx.center(
                    rx.select(
                        values_info["Afin"]["range"][0],
                        value1=ParamState.value1,
                        on_change=ParamState.change_value1
                    ),
                ),
                rx.center(
                    rx.select(
                        values_info["Afin"]["range"][1],
                        value2=ParamState.value2,
                        on_change=ParamState.change_value2
                    ),
                )
            )
        ),
        rx.cond(
            FormState.value == "Multiplicativo",
            rx.hstack(
                rx.text("Parametros: "),
                rx.center(
                    rx.select(
                        values_info["Multiplicativo"]["range"],
                        value1=ParamState.value1,
                        on_change=ParamState.change_value1
                    ),
                ),
            )
        ),
        rx.cond(
            FormState.value == "RSA",
            rx.hstack(
                rx.text("Parametros: "),
                rx.center(
                    rx.select(
                        values_info["RSA"]["range"][0],
                        value1=ParamState.value1,
                        on_change=ParamState.change_value1
                    ),
                ),
                rx.center(
                    rx.select(
                        values_info["RSA"]["range"][1],
                        value2=ParamState.value2,
                        on_change=ParamState.change_value2
                    ),
                )
            )
        ),
        rx.cond(
            FormState.value == "Permutacion",
            rx.hstack(
                rx.text("Parametros: "),
                rx.center(
                    rx.text_area(
                        placeholder="Ingrese m (numero de letras por cluster)",
                        value1=ParamState.value1,
                        on_change=ParamState.change_value1,
                        size="1",
                        variant="surface",
                        resize="both",
                        min_length=1,
                    ),
                ),
                rx.center(
                    rx.text_area(
                        placeholder="Ingrese permutación (ejemplo: 3 1 0 2)",
                        value2=ParamState.value2,
                        on_change=ParamState.change_value2,
                        size="1",
                        variant="surface",
                        resize="both",
                        min_length=1,
                    ),
                ),
            )
        ),
    )