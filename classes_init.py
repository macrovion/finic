class Field:
    """Base class for all contact fields, stores a value."""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Represents a contact's name, inherits from Field."""
    pass
