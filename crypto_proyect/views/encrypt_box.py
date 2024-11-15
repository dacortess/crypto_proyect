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
        #print(params)
        self.is_loading = True
        if "".join(pre_text.split()) != "":
            try:
                self.processed_text, self.possible_keys = methods[method](pre_text.replace(" ", ""), *(int(params[0]), int(params[1])))
            except Exception as e:
                raise(e)
            finally:
                self.is_loading = False
        else:
            self.processed_text = ""
            self.possible_keys = ""




def encrypt_box() -> rx.Component:
    return rx.vstack(
        #rx.text(f"{FormState.value} {TextAreaState.text}"), # Debug
        rx.heading(
            f"Encrypt Message", 
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
                    parameters(),
                ),
                rx.spacer(),
                rx.button(
                    "Encrypt",
                    color_scheme = "blue",
                    loading = CryptoProcess.is_loading,
                    on_click = CryptoProcess.process_text(FormState.value, TextAreaState.text, (ParamState.value1, ParamState.value2))
                ),
            ),
            style={
                "flex-direction": ["column", "row"],  # Cambia a "row" en pantallas grandes
                "width": "100%",                      # Para que ocupe todo el ancho
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
            loading = CryptoProcess.is_loading
        ),
        padding = "2%",
        width = "100%"
    ) 

class ParamState(rx.State):
    value1: str = "1"
    value2: str = "1"

    @rx.event
    def change_value1(self, value1: str):
        self.value1 = value1
    
    @rx.event
    def change_value2(self, value2: str):
        self.value2 = value2
        



def parameters() -> rx.Component:
    return rx.hstack(
        rx.cond(
            FormState.value == "Desplazamiento",
            rx.hstack(
                rx.text("Parametros: "),
                rx.center(
                    rx.select(
                        values_info["Desplazamiento"]["range"],
                        value1 = ParamState.value1,
                        on_change = ParamState.change_value1
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
                        value1 = ParamState.value1,
                        on_change = ParamState.change_value1
                    ),
                ),
                rx.center(
                    rx.select(
                        values_info["Afin"]["range"][1],
                        value2 = ParamState.value2,
                        on_change = ParamState.change_value2
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
                        value1 = ParamState.value1,
                        on_change = ParamState.change_value1
                    ),
                ),
            )
        ),
    )
