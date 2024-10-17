student={
    'vidhi':{
        'fname':'Vidhi',
        'mname':'Bharatbhai',
        'lname':'Nagar',
        'marks':{
            'python':80,
            'c++':85,
            'java':82,
        }
    },
    'mittal':{
        'fname':'Mittal',
        'mname':'Sureshbhai',
        'lname':'Prajapati',
        'marks':{
            'python':89,
            'c++':87,
            'java':80,
        }
    },
    'lalit':{
        'fname':'Lalit',
        'mname':'Diparam',
        'lname':'Prajapati',
        'marks':{
            'python':79,
            'c++':80,
            'java':75,
        }
    },
}


for i in student:
    print(i)
    for x,y in student[i].items():
        print(x,"=",y)
        