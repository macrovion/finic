from main_classes import AddressBook
from general_functions import input_error
from classes_init import Field
import re

class Email (Field):
    def __init__(self, mail):
        self.checking(mail)
        super().__init__(mail)

    def checking (self, mail):
        pattern = r'^.+@.+\.+$'
        if re.match(pattern, mail) is None:
            raise ValueError("Enter correct email")
        
# Робота з поштою
@input_error
def add_email(args, book: AddressBook):
    name, mail = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.adding_email(mail)
    return f"Email added for {name}."

@input_error
def remove_email(args, book: AddressBook):
    name = args [0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.email = None
    return f"Email removed for {name}."

@input_error
def change_email(args, book: AddressBook):
    name, new_email = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.email = new_email
    return f"Email changed for {name}."