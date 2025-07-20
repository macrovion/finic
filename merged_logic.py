
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from main_classes import AddressBook

from general_functions import parse_input, save_data, load_data, format_output_table, \
    get_command_table, print_command_list
from phone import add_contact, delete_contact, change_contact, all_contacts, search_contacts, show_phone
from birthday import add_birthday, show_birthday, birthdays
from address import add_address, remove_address, change_address
from tag import add_tag, remove_tag, show_all_tags, search_by_tags
from email_utils import add_email, remove_email, change_email

from notebook import load_notebook, save_notebook

commands = {
    "hello": "Greet the user",
    "close/exit": "Exit the application",
    "add_contact": "Add a contact",
    "change_contact": "Modify a contact",
    "show_phone": "Show the contact's phone number",
    "all_contacts": "Show all contacts",
    "add_birthday": "Add a birthday to a contact",
    "birthdays": "Show a contact's birthday",
    "upcoming_birthdays": "Show upcoming birthdays",
    "search_contacts": "Search for a contact",
    "delete_contact": "Delete a contact",
    "add_address": "Add address to contact",
    "remove_address": "Remove address from contact",
    "change_address": "Change address of contact",
    "add_tag": "Add a tag",
    "remove_tag": "Remove a tag",
    "search_by_tags": "Search contacts by tags",
    "show_all_tags": "Show all tags",
    "add_email": "Add an email",
    "remove_email": "Remove an email",
    "change_email": "Changing an email",

    "note_add":       "Add note: note_add <text>",
    "note_find":      "Find by text: note_find <string>",
    "note_edit":      "Edit a note: note_edit <index> <new_text>",
    "note_delete":    "Delete note: note_delete <index>",
    "note_tag":       "Add tags: note_tag <index> <tag1,tag2,...>",
    "note_tagfind":   "Find by tag: note_tagfind <tag>"
    }

# Головна програма
def main():
    book = AddressBook()
    notes = load_notebook() 
    print("Welcome to the assistant bot!")
    print_command_list(commands)

    command_completer = WordCompleter(list(commands.keys()), ignore_case=True)

    while True:
        user_input = prompt(">>> ", completer=command_completer)
        if not user_input.strip():
            continue

        command, *args = parse_input(user_input.strip())
        message = ""

        match command:
            case "close" | "exit":
                save_data(book, args[0] if args else "addressbook.pkl")
                message = "Good bye!"

            case "hello":
                book = load_data(args[0] if args else "addressbook.pkl")
                message = "How can I help you?"

            case "show_all_commands" | "help":
                message = get_command_table(commands)

            case "add_contact":
                message = add_contact(args, book)

            case "change_contact":
                message = change_contact(args, book)

            case "delete_contact":
                message = delete_contact(args, book)

            case "search_contacts":
                message = search_contacts(args, book)

            case "show_phone":
                message = show_phone(args, book)

            case "all_contacts":
                message = all_contacts(book)

            case "add_birthday":
                message = add_birthday(args, book)

            case "show_birthday":
                message = show_birthday(args, book)

            case "birthdays":
                message = birthdays(args, book)

            case "add_address":
                message = add_address(args, book)

            case "remove_address":
                message = remove_address(args, book)

            case "change_address":
                message = change_address(args, book)

            case "add_tag":
                message = add_tag(args, book)

            case "remove_tag":
                message = remove_tag(args, book)

            case "search_by_tags":
                message = search_by_tags(book)
            
            case "add_email":
                message = add_email(args, book)

            case "remove_email":
                message = remove_email(args, book)
            
            case "change_email":
                message = change_email(args, book)

            case "note_add":
                text = " ".join(args)
                notes.add_note(text)
                save_notebook(notes)
                message = "Нотатку додано."

            case "note_find":
                found = notes.search_text(" ".join(args))
                if not found:
                    message = "Нічого не знайдено."
                else:
                    message = "\n".join(
                        f"{i}: {n.text} [{', '.join(n.tags)}]"
                        for i, n in enumerate(found)
                    )

            case "note_edit":
                idx = int(args[0])
                new_text = " ".join(args[1:])
                if notes.edit_note(idx, new_text):
                    save_notebook(notes)
                    message = "Нотатку оновлено."
                else:
                    message = "Невірний індекс."

            case "note_delete":
                idx = int(args[0])
                if notes.delete_note(idx):
                    save_notebook(notes)
                    message = "Нотатку видалено."
                else:
                    message = "Невірний індекс."

            case "note_tag":
                idx = int(args[0])
                tags = args[1].split(",")
                if notes.add_tags(idx, tags):
                    save_notebook(notes)
                    message = "Теги додано."
                else:
                    message = "Невірний індекс."

            case "note_tagfind":
                tag = args[0]
                found = notes.search_tag(tag)
                if not found:
                    message = "Нічого не знайдено."
                else:
                    message = "\n".join(
                        f"{i}: {n.text} [{', '.join(n.tags)}]"
                        for i, n in enumerate(found)
                    )

            case _:
                message = "Invalid command. Type `show_all_commands` or `help` to see available commands."

        # Виводимо результат в таблиці
        print(format_output_table("Result", message))


# Запуск тільки як скрипт
if __name__ == "__main__":
    main()
