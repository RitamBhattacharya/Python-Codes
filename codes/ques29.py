# write a program to input a list of numbers and test if a number is equal to the sum of
# the cubes of its digits. Print that new list and find the smallest and greatest element of
# that list.

list=[]
ans=[]
n=int(input("Enter the size of the list:"))
for i in range(n):
    a=int(input(f"Enter element {i+1}:"))
    list.append(a)

def fun(n):
    temp=n
    s=0
    while temp>0:
       s+=pow(temp%10,3)
       temp=temp//10 
    if s==n:
        ans.append(s)


for i in list:
    fun(i)  
        
print(ans)        