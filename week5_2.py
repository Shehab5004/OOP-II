a=input("enter a: ")
b=input("enter b: ")
print(a,type(a))
a= int(a)
b= int(b)
print(a,type(a))
x = lambda a, b: a * b
print(x(a,b))

#list comp

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

oldlist=[2,7,10,15,8]
newlist= [x for x in oldlist if x%2 != 0]
print(newlist)

def myfunc(a):
  return len(a)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
print(list(x))


def square(n):
  return n**2
x= map(square,(5,6,7))
print(x)
print(list(x))
