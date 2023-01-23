# Write a Python script to find HCF (GCD) and LCM of two numbers.

def gcd(a,b):
    if a%b==0:
        return b;
    return gcd(b,a%b)

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print(f"GCD of {a} and {b} is:",gcd(a,b))

lcm=(a*b)/gcd(a,b)
print(f"LCM of {a} and {b} is:",lcm)