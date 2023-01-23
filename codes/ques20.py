# Given a list of integers, write a program to find those which are palindromes.

list=[]
n=int(input("Enter the no of items:"))
for i in range(n):
    a=int(input(f"Enter item no {i+1}:"))
    list.append(a)

def palindrome(x):
    temp=x
    sum=0
    while temp>0:
        sum=sum*10+temp%10
        temp=temp//10
    if(sum==x):
        print(sum,end="  ")    

for i in list:
    palindrome(i)   