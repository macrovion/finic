import datetime
from classes_init import Field
from general_functions import input_error


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


# Робота з днями народжень
@input_error
def add_birthday(args, book):
    if len(args) < 2:
        return "Please provide both name and value."
    name, bday_str = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.adding_birthday(bday_str)
    return f"Birthday added for {name}."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if not record or not record.birthday:
        return "Birthday not found."
    return record.birthday.value.strftime("%d.%m.%Y")

@input_error
def birthdays(book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in the next week."
    result = []
    for item in upcoming:
        result.append(f"{item['name']} - {item['congratulation_date']}")
    return "\n".join(result)