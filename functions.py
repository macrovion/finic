from classes_init import AddressBook, Record, Tag
import pickle

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# Обробка помилок через декоратор
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name, phone or birthday, please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments."
        except:
            return "Something went wrong"
    return inner


# Функції асистента
# Операційні функції програми
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def save_data(book, filename):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook() 

# Користувацькі функції
@input_error
def add_contact(args, book: AddressBook):
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
def add_birthday(args, book: AddressBook):
    name, bday_str = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.adding_birthday(bday_str)
    return f"Birthday added for {name}."

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record or not record.birthday:
        return "Birthday not found."
    return record.birthday.value.strftime("%d.%m.%Y")

@input_error
def birthdays(book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in the next week."
    result = []
    for item in upcoming:
        result.append(f"{item['name']} - {item['congratulation_date']}")
    return "\n".join(result)

@input_error
def add_tag(args, book: AddressBook):
    name, tag_value = args
    record = book.find(name)
    if not record:
        return "Contact not found."

    tag = Tag(tag_value)
    record.tags.add(tag.value)
    return f"Tag '{tag.value}' added to {name}."


@input_error
def remove_tag(args, book: AddressBook):
    name, tag_value = args
    record = book.find(name)
    if not record:
        return "Contact not found."

    if tag_value.lower() in record.tags:
        record.tags.discard(tag_value.lower())
        return f"Tag '{tag_value}' removed from {name}."
    else:
        return f"{name} does not have tag '{tag_value}'."

@input_error
def search_by_tags(book: AddressBook):
    # Доповнення введення
    all_tags = list(Tag.set_of_tags)
    tag_completer = WordCompleter(all_tags, ignore_case=True)

    user_input = prompt("Enter tags to search (separated by spaces): ", completer=tag_completer)
    args = user_input.strip().split()
    
    # Пошук по тегам
    search_tags = set(tag.lower() for tag in args)
    if not search_tags:
        return "Please provide at least one tag to search."

    results = []
    for record in book.data.values():
        if search_tags.issubset(record.tags):
            phones = ", ".join(phone.value for phone in record.phones) if record.phones else "No phones"
            birthday = record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "No birthday"
            tags = ", ".join(record.tags) if record.tags else "No tags"
            results.append(f"{record.name.value}: Phones: {phones}; Birthday: {birthday}; Tags: {tags}")

    if not results:
        return "No contacts found with all of these tags."

    return "\n".join(results)



commands = {
    "hello": "Greet the user",
    "close/exit": "Exit the application",
    "add_contact": "Add a contact",
    "change_contact": "Modify a contact",
    "phone": "Show the contact's phone number",
    "all_contacts": "Show all contacts",
    "add_birthday": "Add a birthday to a contact",
    "show_birthday": "Show a contact's birthday",
    "upcoming_birthdays": "Show upcoming birthdays",
    "search_contacts": "Search for a contact",
    "delete_contact": "Delete a contact",
    "add_note": "Add a note",
    "edit_note": "Edit a note",
    "delete_note": "Delete a note",
    "search_notes": "Search for a note",
    "all_notes": "Show all notes",
    "add_tag": "Add a tag to a note",
    "remove_tag": "Remove a note's tag"
    }

