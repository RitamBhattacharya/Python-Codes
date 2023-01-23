# 51. Write a Python script to create Simple Calculator on user choice.

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    
    a=int(input("Enter your choice:"))
    
    if a==1:
        op1=float(input("Enter first operand:"))
        op2=float(input("Enter second operand:"))
        print(f"{op1}+{op2} = {op1+op2}")
        
    elif a==2:
        op1=float(input("Enter first operand:"))
        op2=float(input("Enter second operand:"))
        print(f"{op1}-{op2} = {op1-op2}")
        
    elif a==3:
        op1=float(input("Enter first operand:"))
        op2=float(input("Enter second operand:"))
        print(f"{op1}*{op2} = {op1*op2}")
        
    elif a==4:
        op1=float(input("Enter first operand:"))
        op2=float(input("Enter second operand:"))
        print(f"{op1}/{op2} = {op1/op2}")
    
    elif(a==5):
        break
    else:
        print("Enter Valid Choice")        
