from main_classes import AddressBook
from general_functions import input_error
from classes_init import Field


class Address(Field):
    def __init__(self, value):
        super().__init__(value)


# Робота з адресами
@input_error
def add_address(args, book: AddressBook):
    if len(args) < 2:
        return "Please provide both name and value."
    name, address = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.adding_address(address)
    return f"Address added for {name}."

@input_error
def remove_address(args, book: AddressBook):
    name = args [0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.removing_address()
    return f"Address removed for {name}."

@input_error
def change_address(args, book: AddressBook):
    name, new_address = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.editing_address(new_address)
    return f"Address changed for {name}."
