# Write a python program to create an 3X3 Matrix randomly and calculate sum of
# the diagonal elements.

from numpy import random
a=random.randint(100,size=(3,3))
print("Random 3*3 matrix:")
print(a)

s=0
for i in range(3):
   s+=a[i][i]

print(f"sum of diagonal elements is:{s}")    