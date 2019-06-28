import pandas as pd

numbers = [11, 22, 33, 44, 55]
s1 = pd.Series(numbers)

ages = {"john":20, "jennie":30, "jim":40, "jack":50, "joe":60}
s2 = pd.Series(ages)

print(s2)

# Access Elements:
print(s1[0])
print(s2["jennie"])

# Slice Elements:
print(s1[1:])
print(s2[2:])
print(s1[2:5])                 # go till 4 .... 5 not included

print(s2["jim":])
print(s2["jim":"joe"])         # here it will go from jim and jack ... joe is not included
