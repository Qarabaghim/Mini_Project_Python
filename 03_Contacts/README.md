# 📞 PhoneBook

A simple PhoneBook application built with **Python** and **Streamlit**.

## Features

- Add new contacts
- View all saved contacts
- Search contacts by name
- Edit existing contacts
- Delete contacts
- Save data permanently using JSON
- Phone number validation:
  - Must start with "09"
  - Must contain exactly 11 digits
  - Only numeric characters are allowed


## Installation

1. Clone the repository:

```bash

git clone https://github.com/Qarabaghim/Mini_Project_Python
cd 03_Contacts\src
```

2. Install dependencies:

```bash

pip install streamlit
```

3. Run the application:

```bash
streamlit run Contacts.py
```

## How It Works

**When the application starts:**

1. Checks whether "phonebook.json" exists.
2. Loads saved contacts into memory.
3. Allows the user to manage contacts through the Streamlit interface.
4. Automatically updates the JSON file after adding, editing, or deleting contacts.


## Project Structure

```text
project/
│
├── Contacts.py
├── phonebook.json
├── requirments.txt
└── README.md
```


## Contact Format

| Valid examples | Invalid examples |
| ----- | --------- |
| 09123456789    | 9123456789  |
| 09351234567    | 091234567890  |
| 09901234567    | 09abcdefgh       |


## Future Improvements

- Duplicate contact prevention
- Contact categories
- Export to CSV
- SQLite database support
- User authentication
- Dark mode UI improvements


## Author

Developed with Python and Streamlit for learning and practice purposes.