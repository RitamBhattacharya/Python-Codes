# Write a Python program using function check whether a number is an Automorphic
# Number or not. In mathematics, an automorphic number is a number whose square
# "ends" in the same digits as the number itself. For example, 5 = 25, 6 = 36, 76 =
# 5776, and 890625 = 793212890625, so 5, 6, 76 and 890625 are all automorphic
# numbers.

n=int(input("Enter the number:"))
m=n**2
a=str(n)
b=str(m)
if b.endswith(a):
    print("auto morphic")
else:
    print("Not a auto morphic")       