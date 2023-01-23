#Write a python program to find mean and median of a set of elements.
list=[1,2,4,5,3,6,19,1]
list.sort()

mean=sum(list)/len(list)

if(len(list)%2==0):
    median=(list[len(list)//2]+list[len(list)//2-1])/2
else:
    median=list[len(list)//2]
    
print(mean)
print(median)        