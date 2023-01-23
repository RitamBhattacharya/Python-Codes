#Write a Python program to print every integer between 1 and n divisible by m. Also
#report whether the number that is divisible by m is even or odd.

n=int(input("Enter the value of n:"))
m=int(input("Enter the value of m:"))

for i in range(n):
    if (i+1)%m==0:
        print(f"{i+1} is divisible by {m}")
        if(i+1)%2==0:
            print(f"{i+1} is even")
        else:
            print(f"{i+1} is odd")    