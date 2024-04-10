import mysql.connector
try:
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="believer-007"
            )
    mycursor = mydb.cursor()
    mycursor.execute("SET autocommit = 1")
    mycursor.execute(f"USE Shop;")
    ProductID = input("Enter Product ID: ")
    ProductName = input("Enter Product Name: ")
    ProductRate = input("Enter Product Rate: ")
    MFD = input("Enter MFD: ")
    mycursor.execute(f"INSERT INTO Products VALUES('{ProductID}', '{ProductName}', '{ProductRate}', '{MFD}')")
    print(f"Vaues Inserted to Products Table")
    mydb.close()

except Exception as e:
    print(f"Error: {e}") 



