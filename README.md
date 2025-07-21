# finic  
finic_project_by_NPT
main

## Personal Assistant Application

### Overview
A command-line personal assistant for managing contacts and notes, featuring birthdays, tags, email/phone validation, and more.

### Features
- Add, search, edit, and delete contacts with phone and email validation  
- Track upcoming birthdays  
- Create, search, edit, and delete notes  
- Tag notes and search by tags  
- Command-line interface with autocomplete and error handling  

---

### Installation

#### 1. Clone the repository
```bash
git clone https://github.com/your-username/finic_project_by_NPT.git
cd finic_project_by_NPT
```

#### 2. Create a virtual environment
```bash
python3 -m venv venv
```

#### 3. Activate the virtual environment
- On Windows:
  ```bash
  venv\\Scripts\\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

#### 4. Install dependencies
```bash
pip install -r requirements.txt
```

> Make sure the `requirements.txt` includes all needed packages, e.g. `prompt_toolkit`, `prettytable`, etc.

---

### Usage
Run the assistant bot:
```bash
python main.py
```
Use the command autocomplete and follow prompts to manage your contacts and notes.

---

### Extensibility
- Modular architecture allows easy feature addition (e.g., voice commands, additional contact fields)  
- Separate modules for contacts, notes, tags, birthdays, and emails  

---

### Troubleshooting
- Ensure Python 3.7 or newer is installed  
- Activate the virtual environment before running or installing packages  
- Update pip if you encounter installation issues:
```bash
python -m pip install --upgrade pip
=======
# Personal Assistant Application

## Overview
A command-line personal assistant for managing contacts and notes, with features for birthdays, tags, and input validation.

## Features
- Store, search, edit, and delete contacts (with phone/email validation)
- List upcoming birthdays
- Create, search, edit, and delete notes
- Tag notes and search/sort by tags
- Simple CLI interface

## Usage
1. Ensure you have Python 3.7+
2. Run the application:
   ```bash
   python main.py
   ```
3. Follow the on-screen prompts to interact with your contacts and notes.

## Extensibility
- Modular design for easy addition of new features (e.g., voice control, more fields)
main
