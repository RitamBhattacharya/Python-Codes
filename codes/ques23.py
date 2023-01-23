# Write a python program to convert a decimal number to a number of a given base b.

n=int(input("Enter a number:"))
b=int(input("Enter the base:"))

s=""

while(n>0):
    if(n%b==10):
        s+="A"
    elif(n%b==11):
        s+="B"
    elif(n%b==12):
        s+="C"
    elif(n%b==13):
        s+="D"
    elif(n%b==14):
        s+="E"
    elif(n%b==15):
        s+="F"
    else:
        s+=str(n%b)
    n=n//b
print((s[::-1]))        
