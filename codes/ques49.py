'''49. Write a Python script to find value of following series: y=1+1/2+1/3+...+1/n where is user input.'''

n=int(input("Enter the value of n:"))
s=0
for i in range(1,n+1):
    s+=1/i
print(s)    