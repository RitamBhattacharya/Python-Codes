# Write a Python script to print all Prime numbers between 1 to n.
import math
def prime(n):
    flag=False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            flag=True
            break
    if flag==False:    
        print(n,end=" ")  
      
n=int(input("Enter the number:"))
for i in range(2,n+1):
    prime(i)