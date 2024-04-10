import pickle
n = int(input('Enter total no of student: '))
datastu = {}
for i in range(n):
    print(f'Enter the details of {i+1}th student.')
    name = input('Enter the name of student: ')
    rollno = int(input('Enter the rollno of student: '))
    marks = int(input('Enter the marks of student: '))
    datastu[rollno] = [name, marks]
    
with open('binary.dat', 'wb') as file:
    pickle.dump(datastu, file)

search = " "
newmarks = " "
while search and newmarks:
    search = input('Enter the rollno of student whose marks to be updated: ')
    newmarks = input('Enter the new marks of the student: ')
    try:
        oldmarks = datastu[int(search)][1]
        if search and newmarks:
            datastu[int(search)][1] = newmarks
            print(oldmarks, '------>', newmarks)
    except ValueError:
        print("\n")

with open('binary.dat', 'wb') as file:
    pickle.dump(datastu, file)
