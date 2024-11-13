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
    
    cursor.execute("insert into employee values('e1','mittu','100000')")
    cursor.execute("insert into employee values('e2','vidhi','100050')")
    cursor.execute("insert into employee values('e3','aadi','3245678')")
    cursor.execute("insert into employee values('e4','d','10000')")
    print("table created")
    mydb.commit()
    
except KeyError as e:
    print(e)