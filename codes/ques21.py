# Print the following pattern using Python program
# 1
# 2 1
# 4 2 1
# 8 4 2 1
# 16 8 4 2 1
# 32 16 8 4 2 1
# 64 32 16 8 4 2 1
n=int(input("Enter n:"))
for i in range(n):
    j=i
    while(j>=0):
        print(pow(2,j),end=(" "))
        j-=1
    print()    
        