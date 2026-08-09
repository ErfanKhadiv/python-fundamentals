# Python Fundamentals

Four small console/data projects from early Python practice, covering file I/O, data structures, OOP, and NumPy. Kept together in one repo rather than as four sparse standalone ones — these were stepping stones on the way toward the AI/ML-focused work in [HBALS-TSP](https://github.com/ErfanKhadiv/HBALS-TSP).

| Project | Focus | Highlights |
|---|---|---|
| [`library-management-system/`](library-management-system) | File I/O, CRUD logic | JSON persistence, input validation loops, borrow/return state tracking |
| [`software-company-oop/`](software-company-oop) | Object-Oriented Programming | Abstract base classes, `@property`/`@classmethod`, inheritance, composition |
| [`sales-analysis-numpy/`](sales-analysis-numpy) | NumPy / data analysis | Aggregation, broadcasting, filtering, sorting on a 2D array |
| [`password-manager/`](password-manager) | File I/O, CRUD logic | Same pattern as the library system, applied to account storage |

## Running any project

```bash
cd <project-folder>
python main.py
```

`sales-analysis-numpy` needs `numpy` installed (`pip install numpy`); the rest use only the standard library.

## Note on password-manager

This stores credentials in **plaintext JSON** — fine for a learning exercise on file I/O and CRUD patterns, but not how you'd handle real credentials (should use hashing/encryption, e.g. `bcrypt` or the OS keychain). Included here for the pattern, not as a security reference.
-e 
## License

MIT — see [LICENSE](LICENSE).

