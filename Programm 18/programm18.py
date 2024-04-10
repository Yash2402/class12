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
    mycursor.execute(f"USE {db};")
    mycursor.execute(f"SELECT * FROM {table};")
    data = mycursor.fetchall()
    for row in data:
        print(row)
    mydb.close()
except Exception as e:
    print(f"Error: {e}") 




