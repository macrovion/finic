from dataclasses import dataclass, field
from typing import List
from general_functions import save_data, load_data

@dataclass
class Note:
    """Represents a single note with text and optional tags."""
    text: str
    tags: List[str] = field(default_factory=list)

    def edit_text(self, new_text: str) -> None:
        """Replace note's text with new_text."""
        self.text = new_text

    def add_tag(self, tag: str) -> None:
        """Add a tag to the note if not already present."""
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        """Remove a tag from the note if it exists."""
        self.tags = [t for t in self.tags if t != tag]


class Notebook(list):
    """A list-based collection of Note objects with methods to manipulate them."""

    def add_note(self, text: str, tags: List[str] = None) -> None:
        """Create a new Note and add it to the notebook."""
        tags = tags or []
        self.append(Note(text=text, tags=tags))

    def search_text(self, query: str) -> List[Note]:
        """Return notes whose text contains the query substring (case-insensitive)."""
        return [n for n in self if query.lower() in n.text.lower()]

    def edit_note(self, idx: int, new_text: str) -> bool:
        """Edit text of the note at given index; return True if successful."""
        try:
            self[idx].edit_text(new_text)
            return True
        except IndexError:
            return False

    def delete_note(self, idx: int) -> bool:
        """Delete the note at given index; return True if successful."""
        try:
            self.pop(idx)
            return True
        except IndexError:
            return False

    def add_tags(self, idx: int, tags: List[str]) -> bool:
        """Add tags to the note at given index; return True if successful."""
        try:
            for tag in tags:
                self[idx].add_tag(tag)
            return True
        except IndexError:
            return False

    def search_tag(self, tag: str) -> List[Note]:
        """Return notes containing the specified tag (case-insensitive)."""
        return [n for n in self if tag.lower() in map(str.lower, n.tags)]


def load_notebook(filename="notebook.pkl") -> Notebook:
    """Load Notebook object from file; return empty Notebook if file missing or invalid."""
    nb = load_data(filename)
    return nb if isinstance(nb, Notebook) else Notebook()


def save_notebook(nb: Notebook, filename="notebook.pkl") -> None:
    """Save Notebook object to file."""
    save_data(nb, filename)
