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
    
    cursor.execute("create table new_employee_tbl(eno int, ename char(30), gender char(1), salary float)")
    print("table created...")
    mydb.commit()
    
except KeyError as e:
    print(e)