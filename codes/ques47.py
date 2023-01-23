# Write a Python script to check whether a number is Perfect number or not.
def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==n:
        return True
    return False
        
n=int(input("Enter the number:"))
if(perfect(n)):
    print("Perfect Number")
else:
    print("Not a perfect Number")    