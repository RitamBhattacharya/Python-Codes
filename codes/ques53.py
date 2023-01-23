'''53.Create the following lists using a for loop:
The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.'''
list=[]
str="abcdefghijklmnopqrstuvwxyz"
for i in range(len(str)):
    t=""
    for k in range(i+1):
        t+=str[i]
    list.append(t)    
print(list)    