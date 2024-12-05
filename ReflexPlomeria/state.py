import reflex as rx

class State(rx.State):
    """The app state."""

    stock_data = [
        {"id": 1, "name": "Mouse", "category": "Peripheral", "location": "Room 1", "quantity": 20},
        {"id": 2, "name": "Keyboard", "category": "Peripheral", "location": "Room 1", "quantity": 10},
    ]

    @staticmethod
    def redirect_to_edit_product(product_id: int):
        print("HOLAAAA", type(product_id))
        return rx.redirect(f"/edit-product/{product_id}")

    @staticmethod
    def save_product(product_id: int):
        def handler(inputs):
            # Encuentra el producto y actualiza sus valores
            for product in State.stock_data:
                if product["id"] == product_id:
                    product["name"] = inputs.get("name", product["name"])
                    product["category"] = inputs.get("category", product["category"])
                    product["location"] = inputs.get("location", product["location"])
                    product["quantity"] = int(inputs.get("quantity", product["quantity"]))
                    break
            return rx.redirect("/inventory")  # Redirigir a la página de inventario después de guardar

        return handler
