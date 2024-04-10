import pickle
n = int(input('Enter total no of student: '))
datastu = {}
for i in range(n):
    print(f'Enter the details of {i+1}th student.')
    name = input('Enter the name of student: ')
    rollno = int(input('Enter the rollno of student: '))
    datastu[rollno] = name
    with open('binaryfile.dat', 'wb') as file:
        pickle.dump(datastu, file)
search = " "
while search:
    search = input('Enter the rollno of student to be searched: ')
    with open('binaryfile.dat', 'rb') as file:
        data = pickle.load(file)
        if search:
            print(data[int(search)])
        