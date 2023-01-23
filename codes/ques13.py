# Write a python program to reduce a string of lowercase characters in
# range ascii [‘a’..’z’] by doing a series of operations. In each operation, select a pair of
# adjacent letters that match, and delete them. Delete as many characters as possible

# using this method and return the resulting string. If the final string is empty,
# return Empty String.
# Input-aaabccddd, output-abd,
# Input- abba output-empty string.

str="abba"
ans=[]

for i in range(len(str)):
    if ans==[]:
        ans.append(str[i])
    elif str[i] != ans[len(ans)-1]:
        ans.append(str[i])
    else:
        ans.pop();
print(ans)                