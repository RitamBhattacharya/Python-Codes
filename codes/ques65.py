# Election results of india for the year 2000 is published. Out of 400 seats ‘ABC’ got
# 180, ‘XYZ’ got 200 and ‘MNP’ got rest. Display the result using suitable graphical
# tools.
import matplotlib.pyplot as plt
x=[400,180,200]
y=["ABC","XYZ","MNP"]
plt.pie(x,labels=y)
plt.show()
