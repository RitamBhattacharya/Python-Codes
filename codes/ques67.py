# Plot the curve O(n) and O(n^2).
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,25,1.0)
y1=x
y2=x**2
plt.plot(x,y1,label="0(n)")
plt.plot(x,y2,label="0(n^2)")
plt.legend()
plt.show()