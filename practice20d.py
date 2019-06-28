import pandas as pd

table = pd.read_csv("CityTemps.csv")    # print whole info       CityTemps is name of csv file
print(table)

print("=======================")
print(table["Year"])         # only table of year will be printed
print("=======================")
print(table.iloc[3])         # index location to located specified no of rows
print("=======================")
print(table.head(5))         # will print top 5 results
print("=======================")
print(table.tail(5))         # will print 5 results from below