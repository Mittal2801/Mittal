import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "2801",
        database = "sample"
    )
    if mydb is None:
        print("Database is not connected")
    else:
        print("Database is connected")
        
    cursor = mydb.cursor()
    cursor.execute("create table employee (id varchar(10)primary key,name varchar(10),sal int(15))")
    print("Employee table created")
    
except KeyError as e:
    print(e)