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
    
    empid = input("enter id = ")
    increment = int(input("Increment = "))
    
    sql = "update employee set sal=sal+%s where id = %s"
    val = (increment,empid, )
    cursor.execute(sql,val)
    print("record updated..")
    mydb.commit()
    
except KeyError as e:
    print(e)