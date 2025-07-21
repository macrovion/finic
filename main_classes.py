from collections import UserDict
import datetime
from classes_init import Name

from phone import Phone
from birthday import Birthday
from address import Address
from tag import Tag
from email_utils import Email


class Record:
    """Stores all data related to a single contact."""

    def __init__(self, name):
        """Initialize contact with name and optional fields."""
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = []
        self.email = None
        self.tags = set()

    def add_phone(self, number):
        """Add a phone number to the contact."""
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        """Remove the specified phone number from contact."""
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)
                break

    def edit_phone(self, old_number, new_number):
        """Replace old phone number with a new one."""
        for idx, phone in enumerate(self.phones):
            if phone.value == old_number:
                self.phones[idx] = Phone(new_number)
                break

    def find_phone(self, number):
        """Return the Phone object matching the number or None."""
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None

    def __str__(self):
        """Return a string representation of contact name and phones."""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def adding_birthday(self, value):
        """Set birthday field from a string."""
        self.birthday = Birthday(value)

    def adding_address(self, address):
        """Add an address to the contact's address list."""
        self.address.append(Address(address))

    def removing_address(self):
        """Remove all addresses from contact."""
        self.address = []

    def editing_address(self, new_address):
        """Replace all addresses with a new single address."""
        self.address = Address(new_address)

    def adding_tags(self, value):
        """Add a tag (as string) to the contact's tag set."""
        tag = str(Tag(value))
        self.tags.add(tag)

    def adding_email(self, email):
        """Set the email field for the contact."""
        self.email = Email(email)


class AddressBook(UserDict):
    """Collection of Records indexed by contact name."""

    def __init__(self):
        """Initialize an empty AddressBook."""
        super().__init__()

    def add_record(self, record):
        """Add a Record object to the address book."""
        self.data[record.name.value] = record

    def find(self, name):
        """Return Record by contact name or None if not found."""
        return self.data.get(name, None)

    def delete(self, name):
        """Delete a contact record by name."""
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, days_towards):
        """
        Return list of contacts with birthdays in the next 'days_towards' days.
        Adjusts dates falling on weekends to next Monday.
        """
        congratulation_date = []
        today = datetime.date.today()

        for record in self.data.values():
            if record.birthday:
                bday_this_year = record.birthday.value.replace(year=today.year)

                if bday_this_year < today:
                    bday_this_year = bday_this_year.replace(year=today.year + 1)

                days_left = bday_this_year - today
                weekday = bday_this_year.weekday()

                if days_left < datetime.timedelta(days_towards):
                    if weekday == 5:  # Saturday
                        bday_this_year += datetime.timedelta(days=2)
                    elif weekday == 6:  # Sunday
                        bday_this_year += datetime.timedelta(days=1)

                    congratulation_date.append({
                        "name": record.name.value,
                        "congratulation_date": bday_this_year.strftime("%d.%m.%Y")
                    })

        return congratulation_date
