# Write a Python script to check whether a number is Armstrong number or not.
n=int(input("Enter the number:"))
def count(n):
    c=0
    while(n>0):
        n=n//10
        c+=1
    return c    

def armstrong(n):
    temp=n
    c=count(temp)
    s=0
    while temp>0:
       s+=(temp%10)**c
       temp=temp//10
    if(s==n):
        return True
    else:
        return False    
    
if armstrong(n):
    print("Armstrong Number")
else:
    print("Not a armstrong number")    