# Python program to check if a string has at least one letter and one number
# Examples:
# Input: welcome2ourcountry34
# Output: True
# Input: stringwithoutnum
# Output: False

str=input("Enter the string")
a=d=False
for i in str:
    if i.isalpha():
        a=True
    if i.isdigit():
        d=True   
if a==True and d==True:
    print("True") 
else:
    print("False")            