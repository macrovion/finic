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
