# Write a program to move all duplicate values in a list to the end of the list.

list=[1,2,6,4,7,8,93,2,1,4,5,6,3,8,6]
ans=[]
doublicates=[]

for i in list:
    if i not in ans:
        ans.append(i)
    else:
        doublicates.append(i)

for i in doublicates:
    ans.append(i)
    
print(doublicates)
print(ans)                