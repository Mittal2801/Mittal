course={
    'CCC':{
        'duration':'2 Month',
        'fees':5000,
    },
    'Frontend':{
        'duration':'6 Month',
        'fees':35000,
    },
    'Python':{
        'duration':'3 Month',
        'fees':15000,
    },
    'Tally':{
        'duration':'2 Month',
        'fees':7000,
    },
    'Fullstack':{
        'duration':'8 Month',
        'fees':70000,
    },
}

for i in course:
    # print(i)
    for j in course[i]:
            # print(j,":",course[i][j])
            if j=='fees':
                if course[i][j]>10000:
                    print(i)
                    print(j,":",course[i][j])
                    