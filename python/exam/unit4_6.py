import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Mittalprajapati2801",
)

print(mydb)

try:
    cursor = mydb.cursor()
    cursor.execute("Create database sample_db ")
    cursor.execute("Show databases")
    my = cursor.fetchall()
    print("Database created")
    
    for i in my:
        print(i)
        
except KeyError as e:
    print(e)
