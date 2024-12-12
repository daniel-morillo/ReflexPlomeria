import reflex as rx
import asyncio

from ..UI.base import basePage
from ..navigation import routes


class FormState(rx.State):
    form_data: dict = {}
    is_submited: bool = False

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        self.is_submited = True
        yield
        await asyncio.sleep(3)
        self.is_submited = False
        yield


def add_product_page():

    my_form = rx.form(
            rx.vstack(
                rx.cond(FormState.is_submited, FormState.form_data.to_string(), ""),
                rx.input(
                    placeholder="Nombre del Producto",
                    name="product_name",
                    width = "100%",
                ),
                rx.input(
                    placeholder="Categoria del Producto",
                    name="category",
                    width = "100%",
                ),
                rx.input(
                    placeholder="Ubicacion del Producto",
                    name="location",
                    width = "100%",
                ),
                rx.input(
                    placeholder="Cantidad del Producto",
                    name="quantity",
                    type="number",
                    width = "100%",
                ),
                rx.input(
                    placeholder="Fecha de Ingreso",
                    name="added_at",
                    type="date",
                    width = "100%",
                ),
                rx.button("Submit", type="submit", width = "100%"), #Pensar
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=False,
            align="center",
            justify="center",
        ),
    
    my_child = rx.vstack(
        rx.heading("Agregar Producto"),
        rx.desktop_only(
            rx.box(
                my_form,
                padding="2em",
                
                border_radius="8px",
                box_shadow="lg",
                width="40vw",
                justify="center",
                align="center",
                text_align="center",
            )
        ),
        rx.mobile_and_tablet(
            rx.box(
                my_form,
                padding="2em",
                
                border_radius="8px",
                box_shadow="lg",
                width="65vw",
                justify="center",
                align="center",
                text_align="center",
            ),
        ),
        padding="2em",
        border="1px solid #ddd",
        border_radius="8px",
        box_shadow="lg",
        width="100%",
        justify="center",
        align="center",
        text_align="center",
    )

    return basePage(my_child, hideNavbar=False)