import reflex as rx
from .header import header
def basePage(child: rx.Component , hideNavbar = False ,*args, **kwargs) -> rx.Component:
    if not (isinstance(child, rx.Component)):
        raise ValueError("Child must be a component")
    if hideNavbar:
        return rx.container(
            child,
            rx.color_mode.button(position="top-left"),
        )
    return rx.fragment(
        header(),
        rx.box(
            child,
            width = "100%",
            
        ),
        width = "100%",
        
    )