from decorator import input_error
from classes_init import Field
import re

class Email(Field):
    """Email field that validates the email format on initialization."""
    def __init__(self, mail):
        self.checking(mail)
        super().__init__(mail)

    def checking(self, mail):
        """Check if the email matches a simple pattern, raise ValueError if not."""
        pattern = r'^.+@.+\..+$'
        if re.match(pattern, mail) is None:
            raise ValueError("Enter correct email")

@input_error
def add_email(args, book):
    """Add an email to a contact by name, валідуючи через Email."""
    if len(args) < 2:
        return "Please provide both name and email."
    name = args[0]
    mail = args[1]
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.email = Email(mail)
    return f"Email added for {name}."


@input_error
def remove_email(args, book):
    """Remove email from a contact."""
    if len(args) < 1:
        return "Please provide the contact name."
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.email = None
    return f"Email removed for {name}."


@input_error
def change_email(args, book):
    """Change the email of a contact by валідуючи через Email."""
    if len(args) < 2:
        return "Please provide both name and new email."
    name = args[0]
    new_mail = args[1]
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.email = Email(new_mail)
    return f"Email changed for {name}."

@input_error
def show_email(args, book):
    """Show the current email of a contact."""
    if len(args) < 1:
        return "Please provide the contact name."
    name = args[0]
    record = book.find(name)
    if not record or not record.email:
        return "Email not found."
    return record.email.value