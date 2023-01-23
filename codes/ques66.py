# Display electricity consumption of a customer for 12 months using suitable
# graphical tools.
import matplotlib.pyplot as plt
import random
bill=[]
for i in range(12):
    bill.append(random.randint(1000,2000))
months=["jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
plt.plot(months,bill)
plt.xlabel("Months")
plt.ylabel("Bill")
plt.show()