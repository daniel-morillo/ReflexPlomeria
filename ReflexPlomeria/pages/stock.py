import reflex as rx
from ..UI.header import header
from ..UI.base import basePage

from ..state import State


def inventory_page() -> rx.Component:
    # Dummy data similar to the reference image
    stock_data = [
        {"id": 9, "name": "Mouse 3", "category": "Mouse", "location": "Room 3", "quantity": 100, "added_at": "19-02-2018"},
        {"id": 8, "name": "Keyboard 2", "category": "Keyboard", "location": "Room 3", "quantity": 100, "added_at": "19-02-2018"},
        {"id": 7, "name": "Monitor 3", "category": "Monitor", "location": "Room 3", "quantity": 100, "added_at": "19-02-2018"},
        {"id": 6, "name": "Mouse 2", "category": "Mouse", "location": "Room 2", "quantity": 90, "added_at": "19-02-2018"},
        {"id": 5, "name": "Keyboard 2", "category": "Keyboard", "location": "Room 2", "quantity": 90, "added_at": "19-02-2018"},
        {"id": 4, "name": "Monitor 2", "category": "Monitor", "location": "Room 2", "quantity": 90, "added_at": "19-02-2018"},
        {"id": 3, "name": "Mouse 1", "category": "Mouse", "location": "Room 1", "quantity": 80, "added_at": "19-02-2018"},
        {"id": 2, "name": "Keyboard 1", "category": "Keyboard", "location": "Room 1", "quantity": 88, "added_at": "19-02-2018"},
        {"id": 1, "name": "Monitor 1", "category": "Monitor", "location": "Room 1", "quantity": 88, "added_at": "19-02-2018"},
    ]

    my_child = rx.vstack(
        rx.box(
            rx.text("Items", font_size="2xl", font_weight="bold", margin_bottom="1em"),
            rx.container(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("ID"),
                            rx.table.column_header_cell("Name"),
                            rx.table.column_header_cell("Category"),
                            rx.table.column_header_cell("Location"),
                            rx.table.column_header_cell("Quantity"),
                            rx.table.column_header_cell("Added at"),
                            rx.table.column_header_cell("Actions"),
                            text_align="center",
                        )

                    ),
                    rx.table.body(
                        rx.foreach(
                            stock_data, show_product
                        )
                    ),
                ),
                margin_top="1em",
                width="100%",
                border="1px solid #ddd",
                border_radius="8px",
                padding="1em",
                box_shadow="md",
                text_align="center",
                justify="center",
            ),
            padding="2em",
            width="100%",
            bg="black",
            border_radius="8px",
            box_shadow="lg",
        ),
        bg="#black",
        min_height="100vh",
    )

    # Main UI layout
    return basePage(my_child)


def show_product(inventory: dict):


    return rx.table.row(
        rx.table.cell(inventory["id"], text_align="center", vertical_align="middle"),
        rx.table.cell(inventory["name"], text_align="center", vertical_align="middle"),
        rx.table.cell(inventory["category"], text_align="center", vertical_align="middle"),
        rx.table.cell(inventory["location"], text_align="center", vertical_align="middle"),
        rx.table.cell(inventory["quantity"], text_align="center", vertical_align="middle"),
        rx.table.cell(inventory["added_at"], text_align="center", vertical_align="middle"),
        rx.table.cell(
            rx.button("View", margin_x="10px"),
            rx.button(
                "Edit",
                margin_x="10px",
                on_click=State.redirect_to_edit_product(inventory["id"]),
            ),
            rx.button("Delete", margin_x="10px"),
            text_align="center",
            vertical_align="middle",
        ),
        justify="center",
        align="center",
    )


# Define functions for editing and deleting (placeholder)
def edit_item(item_id):
    print(f"Edit item with ID {item_id}")


def delete_item(item_id):
    print(f"Delete item with ID {item_id}")



