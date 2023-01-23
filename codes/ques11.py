#Write a python program to find out the palindromic prime numbers between a range.
n=int(input("Enter the lower limit:"))
m=int(input("Enter the upper limit:"))

def prime(w):
    flag=False
    for i in range(2,w):
        if w%i==0:
            flag=True
            break
    if flag==False:
        print(w)
            
def palindrome(x):
    temp=x
    s=0
    while temp>0:
        s=s*10+(temp%10)
        temp=temp//10
    if(s==x):
        prime(s)    
    
for i in range(n,m+1):
    palindrome(i)