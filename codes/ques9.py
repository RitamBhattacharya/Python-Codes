# Write a python program to take an input list and removes the element at index 4
# and add it to the 2nd position and also, at the end of the list.

l=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    a=int(input(f"Enter element {i+1}:"))
    l.append(a)
print(l)
b=l.pop(4)
l.insert(2,b)
l.append(b)    
print(l)      