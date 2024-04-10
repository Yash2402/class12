file = open("abc.txt", "r")

data = file.read()  # Data of txt file is stored in data as string.
length = len(data)
print(f"{length} bytes")
file.close()