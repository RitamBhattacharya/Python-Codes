''' A store charges Rs.120 per item if you buy less than 10 items. If you buy between10
and 99 items, the cost is Rs.100 per item. If you buy1000 or more items, the cost is
Rs.70 per item. Write a program that asks the user how many items they are buying
and prints the total cost. '''

items=int(input("Ennter the no of items you want to buy:"))
price=0
if(items<10):
    price=items*120
elif(items>=10 and items<99):
    price=items*100
elif(items>1000):
    price=items*70;
print(price)            

