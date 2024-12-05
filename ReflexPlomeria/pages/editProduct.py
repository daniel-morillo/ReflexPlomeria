import reflex as rx

from ..UI.base import basePage

def edit_product_page(id: str = None) -> rx.Component:

    # Simula cargar los datos del producto usando el ID
    product_data = {"id": 9, "name": "Mouse 3", "category": "Mouse", "location": "Room 3", "quantity": 100, "added_at": "19-02-2018"}

    if not product_data:
        return rx.text("Product not found!", font_size="xl", color="red")
    

    my_child = rx.box(
        rx.text(f"Editing Product: {product_data['name']}", font_size="2xl", font_weight="bold"),
        rx.input(value=product_data["name"], placeholder="Name"),
        rx.input(value=product_data["category"], placeholder="Category"),
        rx.input(value=product_data["location"], placeholder="Location"),
        rx.input(type="number", value=product_data["quantity"], placeholder="Quantity"),
        rx.input(value=product_data["added_at"], placeholder="Added At"),
        rx.button("Save"),
        padding="2em",
        border="1px solid #ddd",
        border_radius="8px",
        box_shadow="lg",
    )

    return basePage(my_child)