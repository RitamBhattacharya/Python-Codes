# Write a Python script to find all roots of a quadratic equation for all possible
# combination of a, b and c.
# A quadratic equation will have two roots which are obtained using the following
# expression
# where is called discriminate.
import math
print("Quadratic Equation: ax^2 + bx + c = 0")
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

discriminate= b**2-4*a*c;

if discriminate>0:
    x1=(-b+math.sqrt(discriminate))/(2*a)
    x2=(-b-math.sqrt(discriminate))/(2*a)
    print(f"roots are real and different. They are {x1} and {x2}")
elif discriminate==0:
    x=-b/(2*a)
    print(f"roots are real and same. They are {x}")

else:
    x=-b/(2*a)
    i=math.sqrt(-discriminate)/(2*a)
    print(f"roots are imaginary and same. then are {x}+{i}i and {x}-{i}i")        