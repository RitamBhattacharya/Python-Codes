# Python program to capitalize the first and last character of each word in a string
# Input: hello world
# Output: HellO WorlD

s="hello world"
w=s.split(" ")
t=""
for i in w:
    t+=i[0].upper()+i[1:-1]+i[-1].upper()+" "

print(t)        