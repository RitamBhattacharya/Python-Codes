# The set of input is given as ages. Then print the status according to the rules
# using python program.
# Age Status
# <2 in born
# 2-10 child

# 11-17 young
# 18-49 adult
# 50-79 old
# >80 very old

ages=[1,3,13,23,67,98]
age_status=[]

for i in ages:
    if i<2:
        age_status.append("in born")
    elif i>=2 and i<=10:
        age_status.append("child")
    elif i>=11 and i<=17:
        age_status.append("young")
    elif i>=18 and i<=49:
        age_status.append("adult")
    elif(i>=50 and i<=79):
        age_status.append("old")
    else:
        age_status.append("very old")                
print(ages)
print(age_status)            