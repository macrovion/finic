from main_classes import AddressBook
import pickle
from prettytable.colortable import ColorTable, Themes

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
