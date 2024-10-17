sci={
    "total":120,
    "M":60,
    "F":50
}
commerce={
    "total":80,
    "M":30,
    "F":50
}
arts={
    "total":50,
    "M":30,
    "F":20
}

all_student={
    "sci1":sci,
    "commerce1":commerce,
    "arts1":arts
    
}
# print(all_student)


all_total=0
male_total=0
female_total=0

for i in all_student:
    for j in all_student[i]:
        # print(j)
        print(all_student[i][j])
        if j=="total":
            all_total=all_total+(all_student[i][j])
            
        if j=="M":
            male_total=male_total+(all_student[i][j])
            
        
        if all_student[i]==commerce or all_student[i]==arts:
            if j=="F":
                female_total=female_total+(all_student[i][j])
                
        if i=="commerce" or i=="arts":
            if j=="F":
                female_total=female_total+(all_student[i][j])
                
                
            
print("Total student=",all_total)
print("Total Male student=",male_total)
print("Commerce and arts female student=",female_total)