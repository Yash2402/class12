import csv

file = open("abc.csv", "r")
r = csv.reader(file)
print(list(r))
