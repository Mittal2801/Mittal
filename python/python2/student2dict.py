student={
    'vidhi':{
        'fname':'Vidhi',
        'mname':'Bharatbhai',
        'lname':'Nagar',
        'python':80,
        'c++':85,
        'java':82,
        },
 
    'mittal':{
        'fname':'Mittal',
        'mname':'Sureshbhai',
        'lname':'Prajapati',
        'python':89,
        'c++':87,
        'java':80,
        },
  
    'lalit':{
        'fname':'Lalit',
        'mname':'Diparam',
        'lname':'Prajapati',  
        'python':79,
        'c++':80,
        'java':75,
        },
    }

total=0
for i in student:
    print(i)
    for x,y in student[i].items():
            print(x,"=",y)
    
            if x=='python' or x=='c++' or x=='java':
                total+=y
    print("total is ",total)
    total=0