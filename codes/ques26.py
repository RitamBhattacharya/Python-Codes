# Write programs to find the sum of the following series: x - x^2 /2! + x^3 /3! - x^4 /4! +
# x^5 /5! - x^6 /6! (Input x)

x=int(input("Enter the value of x:"))
sum=0

def fact(n):
    a=1
    for i in range(2,n+1):
        a*=i
    return a
    
for i in range(1,7):
    if i%2==1:
        sum+=pow(x,i)/fact(i)
    else:
        sum-=pow(x,i)/fact(i)
        
print(sum)            