from decorator import input_error
from classes_init import Field


class Address(Field):
    """Represents the address field of a contact, inherits validation from Field."""
    def __init__(self, value):
        super().__init__(value)

@input_error
def add_address(args, book):
    """Adds an address to a contact by name. Збирає всі слова після імені в одну строку."""
    if len(args) < 2:
        return "Please provide both name and address."
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.adding_address(address)
    return f"Address added for {name}."


@input_error
def remove_address(args, book):
    """Removes the address from a contact."""
    if len(args) < 1:
        return "Please provide the contact name."
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.removing_address()
    return f"Address removed for {name}."


@input_error
def change_address(args, book):
    """Changes the address of a contact. Збирає всі слова після імені в одну строку."""
    if len(args) < 2:
        return "Please provide both name and new address."
    name = args[0]
    new_address = " ".join(args[1:])
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.editing_address(new_address)
    return f"Address changed for {name}."
