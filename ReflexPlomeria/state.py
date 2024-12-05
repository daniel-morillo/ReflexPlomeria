# state.py
import reflex as rx

class State(rx.State):
    """The app state."""

    @staticmethod
    def redirect_to_edit_product(product_id: int):
        print("Redirecting to edit product")
        return rx.redirect(f"/edit-product/{product_id}")
