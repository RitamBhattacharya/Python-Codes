# 36.Remove all duplicates characters from a given string in Python
# Examples:
# Input : abcabcde
# Output : abcde

str="aaaacdeeefr"
s=""
for i in str:
    if i not in s:
        s+=i
print(s)        