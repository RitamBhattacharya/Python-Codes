# Write a short program to find the average of some numbers entered through the
# keyboard.
# Output
# Enter numbers (Enter 'q' to see the average)
# 2 5 7 15 12 q
# Average = 8.2

list=[]
while True:
    a=input("Enter number:")
    if a=='q' or a=='Q':
        print(f"avg is : {sum(list)/len(list)}")
        break
    else:
        list.append(int(a))    
    