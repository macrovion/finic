import datetime
from classes_init import Field
from decorator import input_error


class Birthday(Field):
    """Stores and validates a contact's birthday as a date."""
    def __init__(self, value):
        try:
            self.value = datetime.datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


# Birthday operations
@input_error
def add_birthday(args, book):
    """Adds a birthday to a contact. Parses string and calls adding_birthday()."""
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
    """Returns the birthday of a contact formatted as DD.MM.YYYY."""
    name = args[0]
    record = book.find(name)
    if not record or not record.birthday:
        return "Birthday not found."
    return record.birthday.value.strftime("%d.%m.%Y")


@input_error
def birthdays(args, book):
    """Shows contacts with birthdays in the next N days. Uses get_upcoming_birthdays()."""
    if len(args) != 1 or not args[0].isdigit():
        return "❗ Вкажіть число днів. Приклад: birthdays 7"

    days = int(args[0])
    upcoming = book.get_upcoming_birthdays(days)

    if not upcoming:
        return "Немає іменин у найближчі дні."

    result = []
    for item in upcoming:
        result.append(f"{item['name']} — {item['congratulation_date']}")
    return "\n".join(result)
