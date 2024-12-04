def calculate_formula(a, b):
    return a**2 + b**2 + 2*a*b

# Input from user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("Result of (a + b)^2:", calculate_formula(a, b))

# Lambda function
formula = lambda a, b: a**2 + b**2 + 2*a*b

# Input from user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("Result of (a + b)^2 using lambda:", formula(a, b))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input from user
n = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {n} is:", factorial(n))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input from user
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
