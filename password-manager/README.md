# Password Manager (Console)

A console CRUD app for storing website/username/password entries, with persistent storage in JSON.

## Features
- Add, view, search, and delete saved accounts
- Search by website or username
- Duplicate (website, username) pair prevention
- Data persists across runs via `passwords.json`

## Run
```bash
python main.py
```

## ⚠️ Note
Passwords are stored in **plaintext JSON** — this was built as a file I/O and CRUD exercise, not a production credential store. A real password manager would encrypt entries at rest (e.g. via `cryptography`/`bcrypt`) rather than writing raw JSON.

## What it demonstrates
Same CRUD/file-I/O pattern as `library-management-system`, applied to a different data shape.
