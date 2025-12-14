import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345678"
)

if mydb == True:
    print("Database connected successfully!")
else:
    print("Invalid Connection!")


mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

print("Database 'alx_book_store' created successfully!")

mycursor.close()
mydb.close()

print("Database connection closed.")