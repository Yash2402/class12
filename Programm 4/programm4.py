file = open(r"abc.txt", "r")

lines_list = file.readlines()
length = len(lines_list)
print(f"Total number of lines are {length}")
file.close()
