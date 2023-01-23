# Write Python programs to sum the given sequences up to n terms: 2/9 - 5/13 + 8/17 ....

n=int(input("Enter the value of n:"))
sum=0
for i in range(n):
    if (i+1)%2==1:
        sum+=(2+ 3*i) / (9+ 4*i)
    else:
        sum-=(2+ 3*i) / (9+ 4*i)   
    
print(sum)        