# Python program to check if a given string is binary string or not
# Examples:
# Input: str = "01010101010";
# Output : Yes

str = "01010101010"
flag=True
for i in str:
    if i!='0' and i!='1':
        print("Not a binary String")
        flag=False
        break
    
if(flag==True):
    print("Binary String")    