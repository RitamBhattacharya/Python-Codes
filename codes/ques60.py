# 60. Input two 3X3 Matrixes. Now perform
# a. the addition of two 3X3 Matrixes.
# b. perform the elements-wise multiplication of two 3X3 Matrixes.
# c. perform the Matrix Multiplication of two 3X3 Matrixes.

mat1=[[0,0,0],[0,0,0],[0,0,0]]
mat2=[[0,0,0],[0,0,0],[0,0,0]]
mat3=[[0,0,0],[0,0,0],[0,0,0]]

print("Enter elements in matrix 1::")
for i in range(3):
    for j in range(3):
        mat1[i][j]=int(input())
        
print("Enter elements in matrix 2::")
for i in range(3):
    for j in range(3):
        mat2[i][j]=int(input())


def display(mat):
    for i in range(3):
        for j in range(3):
            print(mat[i][j],end=" ")
        print()            

# Addition
for i in range(3):
    for j in range(3):
        mat3[i][j]=mat1[i][j]+mat2[i][j]
print("Matrix:1")
display(mat1)
print("Matrix:2")
display(mat2)
print("Addition of matrix 1 and matrix 2:") 
display(mat3)  

# Element wise multiplication
for i in range(3):
    for j in range(3):
        mat3[i][j]=mat1[i][j]*mat2[i][j]    
print("Element wise multiplication of matrix 1 and matrix 2:") 
display(mat3) 

# Matrix Multipplication
for i in range(3):
    for j in range(3):
        mat3[i][j]=0
        for k in range(3):
            mat3[i][j]+=mat1[i][k]*mat2[k][j]         
print("Matrix multiplication of matrix 1 and matrix 2:") 
display(mat3)            