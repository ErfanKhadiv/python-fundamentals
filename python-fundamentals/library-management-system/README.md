# Library Management System

A console-based CRUD app for managing a book collection, with persistent storage in JSON.

## Features
- Add, search, borrow, return, and delete books
- Search by title, author, or category
- Input validation (non-empty fields, numeric page counts, menu bounds)
- Duplicate-title prevention
- Data persists across runs via `books.json`

## Run
```bash
python main.py
```

## What it demonstrates
File I/O with JSON, defensive input handling (`while True` retry loops), and separating data operations from the CLI menu loop.
