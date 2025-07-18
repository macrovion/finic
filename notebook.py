
from dataclasses import dataclass, field
from typing import List
from general_functions import save_data, load_data

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



def load_notebook(filename="notebook.pkl") -> Notebook:
    nb = load_data(filename)
    return nb if isinstance(nb, Notebook) else Notebook()

def save_notebook(nb: Notebook, filename="notebook.pkl") -> None:
    save_data(nb, filename)
