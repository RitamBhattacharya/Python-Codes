# Display the marks of two students for 5 subjects using suitable graphical tools.
import matplotlib.pyplot as plt

marks1=[60,70,50,69,78]
marks2=[78,89,34,67,97]
x = [1, 2, 3, 4, 5]
width=0.35

subs=["Physics","Chemistry","Math","Biology","CS"]
plt.bar(x,marks1, width,label="student-1")
plt.bar([i+width for i in x],marks2,width,label="student-2")

plt.xticks(x,subs)
plt.legend()
plt.show()