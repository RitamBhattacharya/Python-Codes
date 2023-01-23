'''1. Use string slicing to perform the following:
a. Take a string of length greater than 2, return a string except 1 st and last
characters.
b. Take 2 strings, s1, and s2 return a new string made of the first, middle and last
char of each input string.
c. Write a python program to take 2 strings, s1 and s2, create a new string by
appending s2 in the middle of s1.'''

# a.
# s=input("Enter a strinng of length > 2:")
# if(len(s)>2):
#     print(s[1:len(s)-1])
# else:
#     print("Enter a valid string")
    
# b.

# s1=input("Enter the first string:")
# s2=input("Enter the second string:")
# s=s1[0]+s1[len(s1)//2]+s1[len(s1)-1]+s2[0]+s2[len(s2)//2]+s2[len(s2)-1]
# print(s)    


# c.
s1=input("Enter string 1:")
s2=input("Enter string 2:")
v=s1[0:len(s1)//2]+s2+s1[len(s1)//2:]
print(v)    