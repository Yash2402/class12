file = open("abc.txt", "r")
lines_list = file.readlines()
n = int(input("Enter total no of line you want: "))
for i in range(n):
    print(lines_list[i], end = "")
file.close
print(file.read())
