import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root123",
    database="template-db"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES;")

for x in mycursor:
    print(x)

print(type(mycursor))

a = ['1', '2', '3']

print(type(a))
