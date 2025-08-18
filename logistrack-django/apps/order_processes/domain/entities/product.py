import uuid


class Product:
    id: uuid.UUID
    sku: str
    name: str
    description: str

    def __init__(self, id: uuid.UUID, sku: str, name: str, description: str):
        self.id = id
        self.sku = sku
        self.name = name
        self.description = description
