def convert_number(n):
    print(f"Decimal: {n}")
    print(f"Binary: {bin(n)}")
    print(f"Octal: {oct(n)}")
    print(f"Hexadecimal: {hex(n)}")

num = int(input("Enter a decimal number: "))

convert_number(num)
