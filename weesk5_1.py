a="hello"
b="b2b2b2"
c="3g3g        "

print(a,b,c)

d= a + " " + b + " " + c
print(d)

e=len(d)
print(e)

print(d[ :-3])

f=d.upper()
print(f)

g=d.lower()
print(g)

h=d.title()
print(h)

i=d.isdigit()
print(i)

j=d.rfind("3g")
print(j)

k=d.capitalize()
print(k)

l=d.isalnum()
print(l)

m=d.count("b2")
print(m)

print(d.rsplit())

print(d.replace("hello", "python"))

print(d.swapcase())
if "a2" in d:
    print("present")
print("a2" in d)
print(d.find("a2"))