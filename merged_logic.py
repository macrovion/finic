
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

import functions as func
from classes_init import AddressBook


# Головна програма
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    func.print_command_list(func.commands)

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

            case "hello":
                book = func.load_data(args[0] if args else "addressbook.pkl")
                message = "How can I help you?"

            case "add_contact":
                message = func.add_contact(args, book)

            case "change_contact":
                message = func.change_contact(args, book)

            case "delete_contact":
                message = func.delete_contact(args, book)

            case "search_contacts":
                message = func.search_contacts(args, book)

            case "show_phone":
                message = func.show_phone(args, book)

            case "all_contacts":
                message = func.all_contacts(book)

            case "add_birthday":
                message = func.add_birthday(args, book)

            case "show_birthday":
                message = func.show_birthday(args, book)

            case "birthdays":
                message = func.birthdays(book)

            case "show_all_commands" | "help":
                message = func.get_command_table(func.commands)

            case "add_address":
                message = func.add_address(args, book)

            case "remove_address":
                message = func.remove_address(args, book)

            case "change_address":
                message = func.change_address(args, book)

            case "add_tag":
                message = func.add_tag(args, book)

            case "remove_tag":
                message = func.remove_tag(args, book)

            case "search_by_tags":
                message = func.search_by_tags(book)

            case _:
                message = "Invalid command. Type `show_all_commands` or `help` to see available commands."

        # Виводимо результат в таблиці
        print(func.format_output_table("Result", message))


# Запуск тільки як скрипт
if __name__ == "__main__":
    main()
