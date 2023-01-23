# Write a program to accept the age of n employees and count the number of persons
# in the following age group: (i) 26 - 35 (ii) 36 - 45 (iii) 46 – 55

emp=[]
n=int(input("Enter the number of employees:"))
for i in range(n):
    a=int(input(f"Enter age of employee {i+1}:"))
    emp.append(a)
c1=0
c2=0
c3=0
for i in emp:
    if i>=26 and i<=35:
        c1+=1
    elif i>=36 and i<=45:
        c2+=1
    elif i>=46 and i<=55:
        c3+=1        
 
print(f"{c1}  {c2}  {c3}")         