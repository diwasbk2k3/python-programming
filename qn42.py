#Extract Odd and Even from the list
a = [1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even: ", even)
print("Odd: ", odd)    
