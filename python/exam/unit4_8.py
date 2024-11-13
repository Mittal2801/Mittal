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
    
    while('True'):
       
        choice = input("like to enter..?")
        print("Welcome to database...!")
        if choice == "1":
            empid = input("id = ")
            name = input("Name = ")
            salary = int(input("Salary = "))
            sql = "insert into employee (id, name, sal) values(%s,%s,%s)"
            val = (empid, name, salary)
            cursor.execute(sql,val)
            mydb.commit()
            
        elif(choice == "2"):
            break
        
        else:
            print("Wrong input")
            
except KeyError as e:
    print(e)