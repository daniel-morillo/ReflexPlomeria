import reflex as rx
from ..UI.base import basePage
from ..state import State

def edit_product_page(product_id: str = None) -> rx.Component:
    """Página de edición de producto."""
    # Asegúrate de convertir `product_id` a un entero si es necesario
    if product_id is None:
        return basePage(
            rx.text("Invalid product ID.", color="red", font_size="xl")
        )

    # Encuentra los datos del producto en el estado global
    product_data = next((item for item in State.stock_data if item["id"] == int(product_id)), None)

    if not product_data:
        return basePage(
            rx.text("Product not found.", color="red", font_size="xl")
        )

    # Renderiza el formulario con los datos del producto
    my_child = rx.box(
        rx.text(f"Editing Product: {product_data['name']}", font_size="2xl", font_weight="bold"),
        rx.input(value=product_data["name"], placeholder="Name", id="name"),
        rx.input(value=product_data["category"], placeholder="Category", id="category"),
        rx.input(value=product_data["location"], placeholder="Location", id="location"),
        rx.input(type="number", value=product_data["quantity"], placeholder="Quantity", id="quantity"),
        rx.button("Save", on_click=State.save_product(int(product_id))),
        padding="2em",
        border="1px solid #ddd",
        border_radius="8px",
        box_shadow="lg",
    )

    return basePage(my_child)


