# Write programs using nested loops to produce the following patterns:
# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F

str="ABCDEF"

for i in range(len(str)+1):
    for j in range(i):
        print(str[j],end=" ")
    print()    