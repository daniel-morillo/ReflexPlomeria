import reflex as rx

from . import routes

class NavState(rx.State):

    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)

    def to_login(self):
        return rx.redirect(routes.LOGIN_ROUTE)

    def to_inventory(self):

        return rx.redirect(routes.INVENTORY_ROUTE)