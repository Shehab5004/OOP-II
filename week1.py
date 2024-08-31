#print
print("hello python")


name="python"
print(name)


age = 45

salary = 14560.8
name = "John"
print(age)
print(salary)
print(name)

#calculation
a = 10
b = 5
add = a + b 
sub = a - b 
mul = a * b 
mod = a % b 
p = a ** b 
print(add) 
print(sub) 
print(mul) 
print(mod) 
print(p)

#true false
a = True
b = False
print(a and b) 
print(a or b) 
print(not a)

#bitwise operators
a = 10
b = 4
print(a & b) 
print(a | b) 
print(~a) 
print(a ^ b) 
print(a >> 2) 
print(a << 2) 

#assignment operators
a = 10
b = a 
print(b) 
b += a 
print(b) 
b -= a 
print(b) 
b *= a 
print(b) 
b <<= a 
print(b)

#if else
i = 20
if (i < 15): 
    print("i is smaller than 15") 
    print("i'm in if Block") 
else: 
    print("i is greater than 15") 
    print("i'm in else Block") 
print("i'm not in if and not in else Block") 

#loop
for i in range(0, 10, 2): 
    print(i) 

#while loop 
count = 0
while (count < 3): 
    count = count + 1
    print("Hello World")

#function
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
evenOdd(354)
evenOdd(767)




