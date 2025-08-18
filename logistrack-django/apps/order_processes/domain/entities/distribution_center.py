import uuid


class DistributionCenter:
    id: uuid.UUID
    name: str
    city: str

    def __init__(self, id: uuid.UUID, name: str, city: str):
        self.id = id
        self.name = name
        self.city = city
