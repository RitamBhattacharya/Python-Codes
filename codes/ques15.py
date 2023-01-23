# Write a Python program that accepts a hyphen-separated sequence of words as
# input and prints the words in a hyphen-separated sequence after sorting them
# alphabetically.
# Sample Input : green-red-yellow-black-white
# Output : black-green-red-white-yellow

s=input("Enter the hyphen separated string:")
v=s.split("-")
v.sort()

for i in range(len(v)-1):
    print(v[i],end="-")
print(v[len(v)-1])    