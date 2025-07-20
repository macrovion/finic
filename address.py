from general_functions import input_error
from classes_init import Field


class Address(Field):
    """Represents the address field of a contact, inherits validation from Field."""
    def __init__(self, value):
        super().__init__(value)


# Address operations
@input_error
def add_address(args, book):
    """Adds an address to a contact by name. Finds the contact and calls adding_address()."""
    if len(args) < 2:
        return "Please provide both name and value."
    name, address = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.adding_address(address)
    return f"Address added for {name}."


@input_error
def remove_address(args, book):
    """Removes the address from a contact. Finds the contact and calls removing_address()."""
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.removing_address()
    return f"Address removed for {name}."


@input_error
def change_address(args, book):
    """Changes the address of a contact. Finds the contact and calls editing_address()."""
    name, new_address = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.editing_address(new_address)
    return f"Address changed for {name}."
