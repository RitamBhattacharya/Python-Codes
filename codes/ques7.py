# Write a program to input 3 sides of a triangle and print whether it is an equilateral,
#scalene or isosceles triangle.

a=int(input("Enter 1st side:"))
b=int(input("Enter 2nd side:"))
c=int(input("Enter 3rd side:"))

if(a==b and b==c):
    print("Equilateral")
elif(a!=b and b!=c and c!=a):
    print("scalene")
else:
    print("Isoscelene")      