'''55.Write programs as per following specifications: Print the length of the
longest string in the list of strings str_list. Precondition : the list will contain
at least one element.'''

str_list=["Ritam","Bhattacharya","Riddhi"]
str=""
l=0
for i in str_list:
    if len(i)>l:
        l=len(i)
        str=i
        
print(str)        