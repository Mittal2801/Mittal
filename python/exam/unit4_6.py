import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2801"
)
print(mydb)

try:
    cursor = mydb.cursor()
    cursor.execute("Create database Sample")
    cursor.execute("Show Databases")
    my = cursor.fetchall()
    print("Database Created")
    
    for i in my:
        print(i)
        
except KeyError as e:
    print(e)