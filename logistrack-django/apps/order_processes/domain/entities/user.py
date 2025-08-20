import uuid


class User:
    id: uuid.UUID
    name: str
    email: str
    address: str

    def __init__(self, id: uuid.UUID, name: str, email: str, address: str):
        self.id = id
        self.name = name
        self.email = email
        self.address = address


