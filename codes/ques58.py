# Write a program to compare two equal sized lists and print the first index
# where they differ.

list1=[]
list2=[]

n=int(input("Enter the size of the list:"))
print("Enter elements for list:1")
for i in range(n):
    list1.append(int(input()))
    
print("Enter elements for list:2")
for i in range(n):
    list2.append(int(input()))

for i in range(n):
    if list1[i]!=list2[i]:
        print(f"index={i}") 
        break       