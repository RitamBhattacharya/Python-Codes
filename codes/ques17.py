# Write a Python function that takes a list and returns a new list with unique elements
# of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

list=[]
n=int(input("Enter the number of items:"))
for i in range(n):
    a=input(f"Enter element {i+1}:")
    list.append(a)

ans=[] 
for i in list:
    if i not in ans:
        ans.append(i)
        
print(ans)           