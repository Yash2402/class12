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
    table = input("Enter Name of Table: ")
    id = input("Enter Product ID You want to Search: ")
    mycursor.execute(f"USE {db};")
    mycursor.execute(f"DELETE FROM {table} WHERE ProductID = '{id}';")
    print(f"Record is Delete whose Product ID is {id}")
    mydb.close()
except Exception as e:
    print(f"Error: {e}") 