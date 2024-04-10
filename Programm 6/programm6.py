file = open("abc.txt", "r")
data = (file.read()).split()
for word in data:
    print(word, end='-')
