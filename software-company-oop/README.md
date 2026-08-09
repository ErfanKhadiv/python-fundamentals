# Software Company Management System (OOP)

A small object-oriented simulation of employees, teams, projects, and payroll at a software company.

## Design
- `Employee` (abstract base class) — defines the shared interface (`work()`, `calculate_bonus()`) via `abstractmethod`
- `Programmer` / `Designer` — concrete subclasses with role-specific bonus logic
- `Task`, `Project` — task tracking with completion state
- `Team`, `Company` — composition: hold collections of `Employee`/`Task` objects, enforce type checks on add

## Concepts demonstrated
- Abstract base classes (`ABC`, `@abstractmethod`)
- `@property` / `@classmethod` (validated `salary` setter, class-level `employee_count`)
- Inheritance (`Programmer`/`Designer` → `Employee`)
- Composition (`Team` holds `Employee`s, `Project` holds `Task`s, `Company` holds `Employee`s)
- Type enforcement via `isinstance` checks

## Run
```bash
python main.py
```

Runs a small simulation: creates employees, forms a team, tracks project tasks, calculates bonuses, and pays salaries.
