import uuid


class Driver:
    id: uuid.UUID
    name: str
    phone: str
    email: str

    def __init__(self, id: uuid.UUID, name: str, phone: str, email: str):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
