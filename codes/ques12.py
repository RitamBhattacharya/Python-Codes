# Write a python program to find the Twins primes between a range( Twin primes are
# pairs of prime numbers that have just one number between them: 5 and 7, 11 and
# 13,and 29 and 31).

n=int(input("Enter lower limit:"))
m=int(input("Enter upper limit:"))


        
def prime(x):
    for i in range(2,x):
        if x%i==0:
            return 0
    return 1    
        
for i in range(n,m+1):
    if(prime(i) and prime(i+2)):
        print(i,"and",i+2)