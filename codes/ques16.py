# Write a Python function to check whether a string is a pangram or not. Pangrams are
# words or sentences containing every letter of the alphabet at least once.
# For example : “The quick brown fox jumps over the lazy dog”

s=input("Enter your string:")
str="abcdefghijklmnopqrstuvwxyz"
flag=False
for i in str:
    if i not in s:
        print("NOT A PANGRAM")
        flag=True
        break

if flag==False:        
    print("PANGRAM")    