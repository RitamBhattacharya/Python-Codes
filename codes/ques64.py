# Take the five marks of a student for a particular subject. Display the data
# graphically using suitable graph.

import matplotlib.pyplot as plt
marks=[87,65,76,45,89]
x=["Exam1","Exam2","Exam3","Exam4","Exam5"]
plt.bar(x,marks)
plt.xlabel("PHYSICS")
plt.ylabel("MARKS")
plt.title("Marks of Ritam")
plt.show()
