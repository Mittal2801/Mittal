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
    cursor.execute("select * from employee")
    rows = cursor.fetchall()
    
    for i in rows:
        print(i)
        
    mydb.commit()
    
except KeyError as e:
    print(e)