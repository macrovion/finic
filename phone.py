from classes_init import Field
from general_functions import input_error

class Phone(Field):
    """Represents a phone number with validation for 10-digit strings."""
    def __init__(self, number):
        self.checking(number)
        super().__init__(number)

    def checking(self, number):
        """Validate that number is a string of exactly 10 digits."""
        if type(number) != str or len(number) != 10 or not number.isdigit():
            raise ValueError("Phone number must be a string of 10 digits.")


# Contact operations
@input_error
def add_contact(args, book):
    """
    Add a new contact or update existing by name and phone.
    Creates a new Record if contact doesn't exist, else adds phone to existing.
    """
    from main_classes import Record
    if len(args) < 2:
        return "Please provide both name and value."
    name, phone = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def delete_contact(args, book):
    """Delete contact by name if exists."""
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    book.delete(name)
    return f"Contact '{name}' has been deleted."


@input_error
def change_contact(args, book):
    """Change an old phone number to a new one for a given contact."""
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.edit_phone(old_phone, new_phone)
    return "Phone changed."


@input_error
def show_phone(args, book):
    """Return all phone numbers of a contact as a comma-separated string."""
    name = args[0]
    record = book.find(name)
    if not record or not record.phones:
        return "No phones found."
    return ", ".join(phone.value for phone in record.phones)

@input_error
def search_contacts(args, book):
    """Search contacts by name containing the query string (case-insensitive)."""
    query = " ".join(args).lower()
    results = []

    for record in book.data.values():
        if query in record.name.value.lower():
            results.append(str(record))

    if not results:
        return "No contacts found."
    return "\n".join(results)
