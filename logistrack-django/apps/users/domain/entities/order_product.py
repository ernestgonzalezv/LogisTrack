from apps.users.domain.entities.product import Product


class OrderProduct:
    product: Product
    quantity: int

    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
