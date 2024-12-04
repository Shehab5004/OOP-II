start = int(input ("Enter the start value: "))  
end = int(input ("Enter the end value: "))  
  
print ("The Prime Numbers in the range are: ")  
for x in range (start, end + 1):  
    if x > 1:  
        for i in range (2, x):  
            if (x % i) == 0:  
                break  
        else:  
            print (x) 