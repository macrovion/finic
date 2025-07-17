from classes_init import Field
from main_classes import AddressBook, Record
from general_functions import input_error

class Phone(Field):
    def __init__(self, number):
        self.checking(number)
        super().__init__(number)

    def checking(self, number):
        if type(number) != str or len(number) != 10:
            raise ValueError("Phone number must be a string of 10 digits.")
        
# Робота з контактами/номерами телефону
@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        return "Please provide both name and value."
    name, phone = args
    print(f"[DEBUG] args: {args}")
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
def delete_contact(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    book.delete(name)
    return f"Contact '{name}' has been deleted."


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.edit_phone(old_phone, new_phone)
    return "Phone changed."

@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record or not record.phones:
        return "No phones found."
    return ", ".join(phone.value for phone in record.phones)

@input_error
def all_contacts(book: AddressBook):
    if not book.data:
        return "Address book is empty."
    result = []
    for record in book.data.values():
        phones = ", ".join(phone.value for phone in record.phones) if record.phones else "No phones"
        bday = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "No birthday"
        result.append(f"{record.name.value}: Phones: {phones}; Birthday: {bday}")
    return "\n".join(result)

@input_error
def search_contacts(args, book: AddressBook):
    query = " ".join(args).lower()
    results = []

    for record in book.data.values():
        if query in record.name.value.lower():
            results.append(str(record))

    if not results:
        return "No contacts found."
    return "\n".join(results)