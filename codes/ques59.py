# Write a program to reverse a list without using another list or in-built
# function.

list=[1,2,3,4,5,6,7,8,9]
n=len(list)

for i in range(n//2):
    temp=list[i]
    list[i]=list[n-1-i]
    list[n-1-i]=temp

print(list)    

