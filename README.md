# Python Fundamentals

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-array%20computing-013243?logo=numpy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

Four practice projects built to consolidate the core of Python as a first language: persisting data to files, designing programs with objects, and analysing numerical data with arrays. They follow a deliberate progression, from procedural console programs that manage data on disk, to an object-oriented model of a small organisation, to vectorised computation with NumPy, which is the foundation of the scientific and machine learning stack. Each project is a single runnable script with its own README covering the design, example output and known limitations.

## Contents

- [Projects at a glance](#projects-at-a-glance)
- [Project summaries](#project-summaries)
- [Concepts and skills covered](#concepts-and-skills-covered)
- [Repository structure](#repository-structure)
- [Setup and running](#setup-and-running)
- [Design notes and possible extensions](#design-notes-and-possible-extensions)
- [License](#license)

## Projects at a glance

| Project | Focus | Key concepts | Requires |
| --- | --- | --- | --- |
| [`library-management-system/`](library-management-system) | File persistence, CRUD | JSON I/O, input validation, state management | Standard library |
| [`password-manager/`](password-manager) | File persistence, CRUD | JSON I/O, duplicate prevention, index-based deletion | Standard library |
| [`software-company-oop/`](software-company-oop) | Object-oriented design | ABCs, inheritance, composition, properties | Standard library |
| [`sales-analysis-numpy/`](sales-analysis-numpy) | Numerical computing | Axis reductions, boolean masks, sorting, broadcasting | NumPy |

## Project summaries

### Library Management System

A console application for managing a book collection. Books are stored as dictionaries in a JSON file and loaded at start-up, so the collection survives between runs. The user can add, list, search (by title, author or category), borrow, return and delete books. Every input goes through a retry loop that rejects empty values, non-numeric page counts and out-of-range menu choices, duplicate titles are refused, and the state of each book (`available` or `borrowed`) is tracked and checked before a borrow or return is allowed. The data operations are separate functions, kept apart from the menu loop that drives them.

### Password Manager

A console application that stores website, username and password entries in a JSON file. It supports adding, viewing, searching (by website or username) and deleting accounts, and it prevents duplicate (website, username) pairs. It applies the same persistence and CRUD pattern as the library project to a different data shape, with deletion by list index instead of by name. It is a file-handling exercise: passwords are stored in plaintext and the project must not be used for real credentials (see the [security note](password-manager/README.md#security-note)).

### Software Company (OOP)

A small object-oriented model of a software company with employees, teams, projects, tasks and payroll. `Employee` is an abstract base class that defines the interface (`work()` and `calculate_bonus()`), and `Programmer` and `Designer` implement it with role-specific bonuses (20% and 15% of salary). `Team`, `Project` and `Company` use composition to hold collections of employees and tasks, and enforce with `isinstance` checks that only valid objects can be added. The script ends with a short simulation that creates employees, builds a team, completes tasks and pays salaries.

### Monthly Sales Analysis (NumPy)

An analysis of a 12-month by 5-product sales matrix using only core NumPy, with no pandas. It produces seven reports: overall statistics, per-month and per-product summaries, boolean-mask filtering, ranking with `argsort`, a broadcast percentage increase per product, and a profit calculation with per-product costs broadcast across every month. The script shows how to replace explicit loops with whole-array operations along a chosen axis.

## Concepts and skills covered

- **Files and persistence:** reading and writing JSON, graceful handling of a missing or unreadable file, saving after every change
- **Program structure:** small single-purpose functions, a menu-driven main loop, validated input helpers
- **Data handling:** lists of dictionaries, searching, filtering, deleting by value and by index
- **Object-oriented programming:** abstract base classes (`ABC`, `@abstractmethod`), inheritance with `super()`, composition, `@property` with a validating setter, `@classmethod`, `@staticmethod`, `__str__`, class-level state
- **Defensive programming:** input validation, type checks with `isinstance`, raising `ValueError` and `TypeError`
- **NumPy:** array creation, `axis=0` and `axis=1` reductions, `argmax`/`argmin`/`argsort`, boolean masking, broadcasting a 1D array against a 2D one, descriptive statistics

## Repository structure

```
python-fundamentals/
├── library-management-system/   # JSON-backed CRUD app
├── password-manager/            # JSON-backed CRUD app
├── software-company-oop/        # OOP design with ABCs and composition
├── sales-analysis-numpy/        # NumPy analysis reports
├── .gitignore
├── LICENSE
└── README.md
```

The two console apps create their data file (`books.json`, `passwords.json`) in the folder you run them from. Both are listed in `.gitignore`, so personal data is never committed.

## Setup and running

Python 3.8 or newer is recommended. Only the sales analysis needs a third-party package:

```bash
pip install numpy      # sales-analysis-numpy only
```

Run a project from its own folder:

```bash
cd library-management-system
python main.py
```

Run the apps from inside their own folder so the JSON file is created and found in the same place each time.

## Design notes and possible extensions

These are practice projects, and each README lists its specific limitations. The main ones, and how they could be addressed, are:

- **Plaintext credentials:** a real password manager would encrypt entries at rest and derive a key from a master password.
- **Exact-match search:** searches compare whole values, so partial and fuzzy matching are natural next steps.
- **Scripts rather than modules:** the console apps run their menu loop at module level. Moving it into a `main()` function would make the code importable and unit-testable.
- **Flat-file storage:** SQLite would suit larger collections and give atomic writes.
- **Tests:** the pure functions (search, borrow, return, bonus calculation) are good candidates for `pytest` unit tests.

## License

MIT. See [`LICENSE`](LICENSE).
