import csv
with open("telephone.csv", "a") as file:
    csvwriter = csv.writer(file)
    n = int(input("Enter Total Number of Records: "))
    for i in range(n):
        print(f"Fill {i+1}th Record.")
        name = input("Enter the name: ")
        s_id = int(input("Enter the Subscriber ID: "))
        brand = input("Enter the Brand of Telephone: ")
        price = int(input("Enter the price of telephone: "))
        csvwriter.writerow([s_id, name, brand, price])
    print("Record successfully added")

with open("telephone.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in list(csvreader):
        print(row)
    search = input("Enter the Subscriber ID of the Subscriber you want to search: ")
    if search:
        for row in list(csvreader):
            if int(row[0]) == int(search):
                print(row)
            else:
                print("No Records Found")
