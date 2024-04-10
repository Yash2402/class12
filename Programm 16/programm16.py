import mysql.connector
try:
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="believer-007"
            )
    mycursor = mydb.cursor()
    mycursor.execute("SET autocommit = 1")

    db = input("Enter Databse Name: ")
    mycursor.execute(f"USE {db};")
    mycursor.execute("CREATE TABLE Products(ProductID varchar(10) Primary Key, ProductName varchar(45), ProductRate decimal(10), MFD date)")
    print(f"Table Created In Databse {db}")
    mydb.close()
except Exception as e:
    print(f"Error: {e}") 