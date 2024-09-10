"""sum"""
list1=[1,3,7,8,2]
sum=0

for i in list1:
    if i%2==0:
        sum+=i
print(sum)

"""add"""
def addition():
    sum=0
    for i in range(1,11):
        if i%2==0:
            sum+=i
    return sum

print(addition)

"""Multiplication"""
num=int(input("Enter a number:"))
def multiplication(num):
    for i in range(1,11):

        if i ==6:

            continue

        if i ==9:

            break

        print(f"{num}*{i} = {num*i}")

multiplication(num)

"""odd count"""
list1 = [1,3,7,8,2]
sum=0
for i in range(len(list1)): 
    if i%2!=0: 
        sum+=list1[i]
print(sum)

"""last task"""
list1=[1,3,5,7,4]
print(list1[-2],list1[2])

list1=[1,3,5,7,4]
list1[-3]=50
print(list1)

list1=[1,3,5,7,4]
list1.pop()
print(list1)

list1=[1,3,5,7,4]
b=list1.copy()
print(b)

b=[1,3,5,7,4]
b.sort()
print(b)

list1=[1,3,5,7,4]
list2=[2,4,6]
list3=list1 +list2
print(list3)