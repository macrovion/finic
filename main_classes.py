from collections import UserDict
import datetime
from classes_init import Name

from phone import Phone
from birthday import Birthday
from address import Address
from tag import Tag
from email_utils import Email

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = []
        self.email = None
        self.tags = set ()

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)
                break

    def edit_phone(self, old_number, new_number):
        for idx, phone in enumerate(self.phones):
            if phone.value == old_number:
                self.phones[idx] = Phone(new_number)
                break

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def adding_birthday(self, value):
        self.birthday = Birthday(value)

    def adding_address(self, address):
        self.address.append(Address(address))

    def removing_address(self):
            self.address = None

    def editing_address(self, new_address):
            self.address = Address(new_address)

    def adding_tags(self, value):
        tag = str(Tag(value))
        self.tags.add(tag)

    def adding_email(self, email):
        self.email = Email(email)

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
     
    def get_upcoming_birthdays(self, days_towards):
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
                    if weekday == 5:  # Якщо субота
                        bday_this_year += datetime.timedelta(days=2)
                    elif weekday == 6:  # Якщо неділя
                        bday_this_year += datetime.timedelta(days=1)

                    congratulation_date.append({"name": record.name.value, "congratulation_date": bday_this_year.strftime("%d.%m.%Y")})

        return congratulation_date

