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
    
    empid = input("id = ")
    sql = "delete from employee where id=%s"
    val = (empid)
    cursor.execute(sql,[val])
    print("Deleted!")
    
    mydb.commit()
    
except KeyError as e:
    print(e)