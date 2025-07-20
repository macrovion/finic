from general_functions import input_error
from classes_init import Field
import re

class Email(Field):
    """Email field that validates the email format on initialization."""
    def __init__(self, mail):
        self.checking(mail)
        super().__init__(mail)

    def checking(self, mail):
        """Check if the email matches a simple pattern, raise ValueError if not."""
        pattern = r'^.+@.+\.+$'
        if re.match(pattern, mail) is None:
            raise ValueError("Enter correct email")
        

# Email operations
@input_error
def add_email(args, book):
    """Add an email to a contact by name, calling record.adding_email()."""
    name, mail = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.adding_email(mail)
    return f"Email added for {name}."


@input_error
def remove_email(args, book):
    """Remove email from a contact by setting record.email to None."""
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.email = None
    return f"Email removed for {name}."


@input_error
def change_email(args, book):
    """Change the email of a contact by directly assigning new_email."""
    name, new_email = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.email = new_email
    return f"Email changed for {name}."
