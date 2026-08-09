from abc import ABC, abstractmethod

class Employee(ABC):

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.salary})"

    @classmethod
    def number_employees(cls):
        return cls.employee_count

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:
            self._salary = new_salary
        else:
            raise ValueError("Salary cannot be negative!")

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def calculate_bonus(self):
        pass


class Programmer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def work(self):
        print("Programmer is coding!")

    def calculate_bonus(self):
        # bonus = %20
        return self.salary * 20 / 100


class Designer(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.tool = tool

    def work(self):
        print("Designer is designing!")

    def calculate_bonus(self):
        # bonus = %15
        return self.salary * 15 / 100


class Task:
    def __init__(self, title, deadline):
        if not self.is_valid_title(title):
            raise ValueError("Title must be at least 3 characters")
        self.title = title
        self.deadline = deadline
        self.completed = False

    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3

    def complete_task(self):
        self.completed = True


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
        else:
            raise TypeError("Only Task objects can be added")

    def check_completion(self):
        return all(task.completed for task in self.tasks)



class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("Only Employee objects can be added")

        if employee in self.members:
            print("Employee is already in the team!")
        else:
            self.members.append(employee)

    def show_all_members(self):
        for member in self.members:
            print(member)


class Company:

    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            raise TypeError("Only Employee objects can be added")

    def show_employees(self):
        for employee in self.employees:
            print(employee)

    def pay_salaries(self):
        for employee in self.employees:
            employee.salary += employee.calculate_bonus()






# Employees
p1 = Programmer("Erfan", 5000, "Python")
p2 = Programmer("Ali", 7000, "Java")

d1 = Designer("Sara", 4000, "Figma")

# Company
company = Company("OpenAI")

company.add_employee(p1)
company.add_employee(p2)
company.add_employee(d1)


print(f"Employees Count: {Employee.number_employees()}")
company.show_employees()
print("-" * 30)

# Team
backend_team = Team("Backend Team")

backend_team.add_member(p1)
backend_team.add_member(p2)

print(f"Team name: {backend_team.name}")
print("Team Members:")
backend_team.show_all_members()
print("-" * 30)

# Tasks
task1 = Task("Login System", "2025-08-01")
task2 = Task("Dashboard UI", "2025-08-10")

print("Task1 completed:", task1.completed)

task1.complete_task()

print("Task1 completed after update:", task1.completed)
print("-" * 30)

# Project
project = Project("Management System")

project.add_task(task1)
project.add_task(task2)

print("Project tasks count:", len(project.tasks))
print(project.check_completion())
task2.complete_task()
print(project.check_completion())

print("-" * 30)

# Bonus Calculation
print("Bonuses:")
print(p1.name, p1.calculate_bonus())
print(p2.name, p2.calculate_bonus())
print(d1.name, d1.calculate_bonus())
print("-" * 30)

# Salaries Before Payment
print("Salaries Before Payment:")
print(p1.name, p1.salary)
print(p2.name, p2.salary)
print(d1.name, d1.salary)
print("-" * 30)

# Pay Salaries (salary + bonus)
company.pay_salaries()

print("Salaries After Payment:")
print(p1.name, p1.salary)
print(p2.name, p2.salary)
print(d1.name, d1.salary)
