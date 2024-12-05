"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .UI.header import header
from .UI.base import basePage
from . import pages
from .state import State
from rxconfig import config



class State(rx.State):
    """The app state."""

    @staticmethod
    def redirect_to_edit_product(product_id: int):
        return rx.redirect(f"/edit-product/{product_id}")

    



def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.container(
        
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
        bg="black",
        min_height="100vh",
        
    )

    return basePage(my_child, hideNavbar=False)


app = rx.App()
app.add_page(pages.edit_product_page, route="/edit-product/[id]")
app.add_page(index)
app.add_page(pages.inventory_page, route="/inventory")

