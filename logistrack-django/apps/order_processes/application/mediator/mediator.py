class Mediator:
    def __init__(self):
        self._handlers = {}

    def register(self, message_type, handler_class):
        self._handlers[message_type] = handler_class

    def send(self, message):
        message_type = type(message)
        if message_type not in self._handlers:
            raise Exception(f"No handler registered for {message_type}")
        handler = self._handlers[message_type]()
        return handler.handle(message)