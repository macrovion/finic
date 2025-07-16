# pip install prettytable
# pip install prompt_toolkit

from prettytable.colortable import ColorTable, Themes
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

import functions as func
from classes_init import AddressBook


# Побудова таблиці для виводу
def format_output_table(title: str, content: str) -> str:
    table = ColorTable(theme=Themes.DEFAULT)
    table.field_names = [title]
    table.align[title] = "l"
    for line in content.strip().split("\n"):
        table.add_row([line])
    return str(table)

# Вивід списку команд
def get_command_table(commands_dict):
    table = ColorTable(theme=Themes.HIGH_CONTRAST)
    table.field_names = ["Command", "Description"]
    table.align["Command"] = "l"
    table.align["Description"] = "r"
    table.add_rows(list(commands_dict.items()))
    return str(table)

def print_command_list(commands_dict):
    print("List of available commands:")
    command_table = get_command_table(commands_dict)
    print(command_table)

# Головна програма
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    print_command_list(func.commands)

    command_completer = WordCompleter(list(func.commands.keys()), ignore_case=True)

    while True:
        user_input = prompt(">>> ", completer=command_completer)
        if not user_input.strip():
            continue

        command, *args = func.parse_input(user_input.strip())
        message = ""

        match command:
            case "close" | "exit":
                func.save_data(book, args[0] if args else "addressbook.pkl")
                message = "Good bye!"
                print(format_output_table("Message", message))
                break

            case "hello":
                book = func.load_data(args[0] if args else "addressbook.pkl")
                message = "How can I help you?"

            case "add":
                message = func.add_contact(args, book)

            case "change":
                message = func.change_contact(args, book)

            case "phone":
                message = func.show_phone(args, book)

            case "all":
                message = func.all_contacts(book)

            case "add-birthday":
                message = func.add_birthday(args, book)

            case "show-birthday":
                message = func.show_birthday(args, book)

            case "birthdays":
                message = func.birthdays(book)

            case "show_all_commands" | "help":
                message = get_command_table(func.commands)

            case _:
                message = "Invalid command. Type `show_all_commands` or `help` to see available commands."

        # Виводимо результат в таблиці
        print(format_output_table("Result", message))


# Запуск тільки як скрипт
if __name__ == "__main__":
    main()
