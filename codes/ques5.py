'''Write a python program to find all occurrences of “India” in given string ignoring the
case.'''

s=input("Enter the string:")
w=s.lower().split(" ")
c=0
for i in w:
    if i=="india":
        c+=1
print(c)        