import csv

def Write(csvwriterobj):
    run = True
    while run:
        userid = input('Enter the User ID: ')
        password = input('Enter the password: ')
        csvwriterobj.writerow([userid, password])
        a = input('Want to enter more User ID [[y]/n]: ')
        if a != 'y':
            run = False

def search(userid, csvreaderobj):
    for row in csvreaderobj:
        if row[0] == userid:
            print(row)

with open("userpassword.csv", "a") as file1:
    csvwriter = csv.writer(file1)
    Write(csvwriter)

searchinput = input('Enter the User ID to be searched: ')
with open("userpassword.csv", "r") as file2:
    csvreader = csv.reader(file2)
    search(searchinput, csvreader)