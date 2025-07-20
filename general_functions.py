import pickle
from prettytable.colortable import ColorTable, Themes

def input_error(func):
    """Decorator that catches common errors and returns user-friendly messages."""
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


@input_error
def parse_input(user_input):
    """Parse user input string into command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def save_data(book, filename):
    """Save the address book object to a file using pickle."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename):
    """Load the address book from a file or create a new one if file not found."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        from main_classes import AddressBook
        return AddressBook()


def format_output_table(title: str, content: str) -> str:
    """Format multiline string content into a colored table with a title."""
    table = ColorTable(theme=Themes.DEFAULT)
    table.field_names = [title]
    table.align[title] = "l"
    for line in content.strip().split("\n"):
        table.add_row([line])
    return str(table)


def get_command_table(commands_dict):
    """Return a formatted colored table of commands and their descriptions."""
    table = ColorTable(theme=Themes.HIGH_CONTRAST)
    table.field_names = ["Command", "Description"]
    table.align["Command"] = "l"
    table.align["Description"] = "r"
    table.add_rows(list(commands_dict.items()))
    return str(table)


def print_command_list(commands_dict):
    """Print the list of available commands in a formatted table."""
    print("List of available commands:")
    command_table = get_command_table(commands_dict)
    print(command_table)
