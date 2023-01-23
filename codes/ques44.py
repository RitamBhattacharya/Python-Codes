# Write a Python script to check whether a number is Prime number or not.
import math
n=int(input("Enter the number:"))
flag=True
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        print("not prime")
        flag=False
        break
if flag==True:
    print("prime")    