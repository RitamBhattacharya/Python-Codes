# Write a program to display the maximum and minimum values from the
# specified range of indexes of list.

l=[3,8,0,8,6,4,444,2,239,4,834,127,111,769,13,444,987,6,6,4,5,3,555,323]
m=int(input("Enter the lower limit:"))
n=int(input("Enter the upper linit:"))
l1=len(l)
if m<0 or n<0 or m>l1 or n>l1:
    print("Invalid Limits!!")
else:
    min=l[m]
    max=l[n]
    for i in range(m+1,n+1):
        if l[i]>max:
            max=l[i]
        if l[i]<min:
            min=l[i]
            
print(f"{min}  {max}")                    