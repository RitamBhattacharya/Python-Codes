# Write a Python Program to print the Prime Factors of an Integer.
def prime(z):
    flag=False
    for i in range(2,z):
        if(z%i==0):
            flag=True
            break
    if(flag==False):
        print(z)
                
n=int(input("Enter the number"))
for i in range (2,n):
    if n%i==0:
        prime(i)