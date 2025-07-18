from classes_init import Field
from general_functions import input_error
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


class Tag(Field):
    set_of_tags = set()

    def __init__(self, value):
        self.__class__.set_of_tags.add(value.lower())
        super().__init__(value.lower())

# Робота з тегами
@input_error
def add_tag(args, book):
    if len(args) < 2:
        return "Please provide both name and value."
    name, tag_value = args
    record = book.find(name)
    if not record:
        return "Contact not found."

    tag = Tag(tag_value)
    record.tags.add(tag.value)
    return f"Tag '{tag.value}' added to {name}."


@input_error
def remove_tag(args, book):
    name, tag_value = args
    record = book.find(name)
    if not record:
        return "Contact not found."

    if tag_value.lower() in record.tags:
        record.tags.discard(tag_value.lower())
        return f"Tag '{tag_value}' removed from {name}."
    else:
        return f"{name} does not have tag '{tag_value}'."


def show_all_tags():
    return list(Tag.set_of_tags)

@input_error
def search_by_tags(book):
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

