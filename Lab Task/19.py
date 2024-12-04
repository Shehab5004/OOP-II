def is_armstrong(num):
    total = 0
    digits = len(str(num)) 
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return num == total
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print(f"Armstrong numbers between {start} and {end} are:")
for i in range(start, end + 1):
    if is_armstrong(i):
        print(i)
