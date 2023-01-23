# Write a Python script to print Fibonacci series up to n terms.
n=int(input("Enter the number:"))
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
for i in range(n):
    print(f"fib[{i}]=",fib(i))