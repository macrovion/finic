from dataclasses import dataclass, field
from typing import List

@dataclass
class Note:
    text: str
    tags: List[str] = field(default_factory=list)

    def edit_text(self, new_text: str) -> None:
        self.text = new_text

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        self.tags = [t for t in self.tags if t != tag]


class Notebook(list):
    def add_note(self, text: str, tags: List[str] = None) -> None:
        tags = tags or []
        self.append(Note(text=text, tags=tags))

    def search_text(self, query: str) -> List[Note]:
        return [n for n in self if query.lower() in n.text.lower()]

    def edit_note(self, idx: int, new_text: str) -> bool:
        try:
            self[idx].edit_text(new_text)
            return True
        except IndexError:
            return False

    def delete_note(self, idx: int) -> bool:
        try:
            self.pop(idx)
            return True
        except IndexError:
            return False

    def add_tags(self, idx: int, tags: List[str]) -> bool:
        try:
            for tag in tags:
                self[idx].add_tag(tag)
            return True
        except IndexError:
            return False

    def search_tag(self, tag: str) -> List[Note]:
        return [n for n in self if tag.lower() in map(str.lower, n.tags)]


# Notebook Assistant - фуекціонал

import storage  # модуль для збереження/завантаження

class notebook_ssistant:
    def __init__(self):
        self.notebook = storage.load()

    def add_note(self, text: str, tags: list = None) -> str:
        self.notebook.add_note(text, tags)
        storage.save(self.address_book, self.notebook)
        return "Нотатку додано"

    def find_note_text(self, query: str):
        return self.notebook.search_text(query)

    def edit_note(self, idx: int, new_text: str) -> str:
        if self.notebook.edit_note(idx, new_text):
            storage.save(self.address_book, self.notebook)
            return "Нотатку оновлено"
        return "Помилковий індекс"

    def delete_note(self, idx: int) -> str:
        if self.notebook.delete_note(idx):
            storage.save(self.address_book, self.notebook)
            return "Нотатку видалено"
        return "Помилковий індекс"

    def add_tag(self, idx: int, tags: list) -> str:
        if self.notebook.add_tags(idx, tags):
            storage.save(self.address_book, self.notebook)
            return "Теги додано"
        return "Помилковий індекс"

    def find_note_tag(self, tag: str):
        return self.notebook.search_tag(tag)
    

# інтерфейс командного рядка notebook_assistant

   # НОТАТКИ
   
        if user.startswith("note add"):
            text = user[9:].strip('" ')
            print(bot.add_note(text))
            continue

        if user.startswith("note tag "):
            idx = int(parts[2])
            tags = parts[3].split(",")
            print(bot.add_tag(idx, tags))
            continue

        if user.startswith("note find"):
            query = user[9:]
            print_notes(bot.find_note_text(query))
            continue

        if user.startswith("note tagfind"):
            print_notes(bot.find_note_tag(parts[2]))
            continue

        if user.startswith("note delete"):
            print(bot.delete_note(int(parts[2])))
            continue


