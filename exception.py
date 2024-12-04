class InvalidVoterException(Exception):
    pass

def check_voter_age(age):
    try:
        if age < 18:
            raise InvalidVoterException("Age is less than 18, invalid voter.")
        print("Valid voter!")
    except InvalidVoterException as e:
        print(e)

# Test
age = int(input("Enter your age: "))
check_voter_age(age)


class SalaryNotInRange(Exception):
    pass

class Employee:
    def __init__(self, name, salary):
        self.name = name
        if salary < 10000 or salary > 50000:
            raise SalaryNotInRange("Salary not in the range 10,000 to 50,000.")
        self.salary = salary

    def display_salary(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

# Test
try:
    name = input("Enter employee name: ")
    salary = int(input("Enter employee salary: "))
    emp = Employee(name, salary)
    emp.display_salary()
except SalaryNotInRange as e:
    print(e)


arr = [10, 5, 15, 20]

try:
    divisor = int(input("Enter divisor: "))
    for num in arr:
        print(num / divisor)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input, please enter an integer.")
except TypeError:
    print("Error: Type mismatch.")
except IndexError:
    print("Error: Index out of bounds.")
except AttributeError:
    print("Error: Invalid attribute access.")
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Execution complete.")


class InsufficientFunds(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientFunds("Withdrawal amount exceeds the current balance.")
            self.balance -= amount
            print(f"Withdrawal successful! Remaining balance: {self.balance}")
        except InsufficientFunds as e:
            print(e)

# Test
balance = int(input("Enter initial balance: "))
account = BankAccount(balance)

amount = int(input("Enter withdrawal amount: "))
account.withdraw(amount)
