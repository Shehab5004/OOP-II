#Inheritance
"""
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        return f"Name: {self.name}, ID: {self.emp_id}"

class PermanentEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class ContractEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

if __name__ == "__main__":
    perm_employee = PermanentEmployee(name="Tamim", emp_id=101, monthly_salary=50000)
    print(perm_employee.display_info())
    print("Permanent Employee Salary: ",perm_employee.calculate_salary())

    contract_employee = ContractEmployee(name="Sakib", emp_id=102, hourly_rate=400, hours_worked=120)
    print(contract_employee.display_info())
    print("Contract Employee Salary: ",contract_employee.calculate_salary())


#Ploymorphism
class Transport:
    def calculate_cost(self, weight, distance):
        raise NotImplementedError("Subclasses must implement this method")

class Truck(Transport):
    def calculate_cost(self, weight, distance):
        return (5*distance)+(2*weight)

class Ship(Transport):
    def calculate_cost(self, weight, distance):
        return (3*distance)+(1*weight)

class Plane(Transport):
    def calculate_cost(self, weight, distance):
        return (10*distance)+(5*weight)

def calculate_delivery_costs(transports, weight, distance):
    for transport in transports:
        mode = transport.__class__.__name__
        cost = transport.calculate_cost(weight, distance)
        print(f"{mode}: Delivery cost is : {cost}")

if __name__ == "__main__":
    truck = Truck()
    ship = Ship()
    plane = Plane()
    transports = [truck, ship, plane]
    calculate_delivery_costs(transports, weight=50, distance=200)

#exception
def divide_elements(values, divisor):
    try:
        results = [value / divisor for value in values]
        return results
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Divisor must be a number.")
values = [10, 20, 30, 40]
divisor = input("Enter the divisor: ")

try:
    divisor = float(divisor)
    print(divide_elements(values, divisor))
except ValueError:
    print("Error: Please enter a valid number.")


class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self, balance, min_balance):
        self.balance = balance
        self.min_balance = min_balance
    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")
try:
    account = BankAccount(1000, 200)
    account.withdraw(500)
    account.withdraw(400)
except InsufficientFundsError as e:
    print(e)


import numpy as np
def calculate_average_and_top_student(scores):
    averages = np.mean(scores, axis=1)
    top_student_index = np.argmax(averages)
    top_average_score = averages[top_student_index]
    print(f"Average scores: {averages}")
    print(f"Student {top_student_index + 1} has the highest average score: {top_average_score}")
scores = np.array([[85, 87, 80],[92, 85, 81],[75, 85, 80],[95, 91, 94]])
calculate_average_and_top_student(scores)


import numpy as np
sales_data = np.array([[100, 150, 120],[200, 180, 210],[300, 250, 275]])

first_three_products_sales = sales_data[:3]
print("Sales data for the first three products:")
print(first_three_products_sales)

last_month_sales = sales_data[:, -1]
print("\nSales data for all products in the last month:")
print(last_month_sales)

specific_sales_data = sales_data[1, 2]
print("\nSales data for the 2nd product in the 3rd month:", specific_sales_data)


import numpy as np

data = np.array([["37", "78.9"], ["12", "45.6"]])

# Convert entire column to integer
data[:, 0] = data[:, 0].astype(int)
print("After converting first column to int:", data)

# Convert entire column to float
data[:, 1] = data[:, 1].astype(float)
print("After converting second column to float:", data)

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

view = arr[1, :]
copy = arr[:, 2].copy()
view[0] = 99
copy[0] = 88
print("Original Array:", arr)
print("View:", view)
print("Copy:", copy)


import numpy as np

arr = np.arange(12)
try:
    reshaped = arr.reshape(4, 3)
except ValueError as e:
    print("Reshape error:", e)
    reshaped = np.pad(arr, (0, 4), 'constant').reshape(4, 4)

print("Reshaped Array:")
print(reshaped)

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

horizontal = np.hstack((arr1, arr2))
vertical = np.vstack((arr1, arr2))

print("Horizontal Join:", horizontal)
print("Vertical Join:", vertical)


import numpy as np
temperatures = np.array([15, 22, 30, 10, 18, 25, 28, 8])
threshold = 20
min_value = 10

high_temp_indices = np.where(temperatures > threshold)[0]
print("Indices where temperature exceeds threshold:", high_temp_indices)

adjusted_temperatures = np.where(temperatures < threshold, min_value, temperatures)
print("Adjusted temperatures:", adjusted_temperatures)


import numpy as np
scores = np.array([85, 75, 90, 80, 70, 95, 60, 88])

indices_75 = np.where(scores == 75)[0]
indices_90 = np.where(scores == 90)[0]

print("Indices of score 75:", indices_75)
print("Indices of score 90:", indices_90)

ascending_scores = np.sort(scores)
print("Scores in ascending order:", ascending_scores)

descending_scores = np.sort(scores)[::-1]
print("Scores in descending order:", descending_scores)


import numpy as np

prices = np.array([15, 25, 35, 45, 55])
filtered = prices[(prices >= 20) & (prices <= 50)]

print("Filtered prices:", filtered)


import numpy as np

data = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
flattened = data.flatten()

print("Flattened Array:", flattened)



class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be greater than zero.")
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__balance}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be greater than zero.")
    def check_balance(self):
        print(f"Current balance: ${self.__balance}")
        return self.__balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(200)
account.withdraw(70)
account.check_balance()
"""


class LibraryBook:
    def __init__(self, ISBN, title, author):
        self.__ISBN = ISBN
        self._title = title
        self._author = author
        self._status = "available"
    def get_ISBN(self):
        return f"***-***-{self.__ISBN[-4:]}"
    def borrow_book(self, borrower_name):
        if self._status == "available":
            self._status = "borrowed"
            print(f"The book '{self._title}' has been borrowed by {borrower_name}.")
        else:
            print(f"The book '{self._title}' is already borrowed.")
    def _display_basic_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        
class DigitalLibraryBook(LibraryBook):
    def __init__(self, ISBN, title, author, file_format):
        super().__init__(ISBN, title, author)
        self._file_format = file_format
    def display_info(self):
        self._display_basic_info()
        print(f"File Format: {self._file_format}")
book1 = LibraryBook("978-3-16-148410-0", "Depressed Soul", "The Great Shehab")
print("Masked ISBN:", book1.get_ISBN())

book1.borrow_book("Alice")
book1.borrow_book("Bob")
digital_book = DigitalLibraryBook("978-1-23-456789-0", "How To Get Poor Marks in Exam", "Shehab The Great", "PDF")
digital_book.display_info()
