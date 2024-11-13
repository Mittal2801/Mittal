import mysql.connector
try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Mittalprajapati2801",
        database = "sample_db"
    )
    
    if mydb is None:
        print("Not connected")
        
    else:
        print("connected")
        
    cursor = mydb.cursor()
    cursor.execute("create table employee (id varchar(10)primary key, name varchar(20), sal numeric(10))")
    print("Employee table created")
    
except KeyError as e:
    print(e)