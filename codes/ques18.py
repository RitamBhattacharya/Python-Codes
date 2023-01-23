# Write a Python function that accepts a string and calculate the number of upper case
# letters and lower case letters. Sample String : ‘The quick Brow Fox’
# Expected Output :
# No. Of Upper case characters : 3
# No. Of Lower case Characters : 12

lc=0
uc=0

s=input("Enter the string:")

for i in s:
    if(i.islower()):
        lc+=1
    elif i.isupper():
        uc+=1

print(f"{lc}  {uc}")