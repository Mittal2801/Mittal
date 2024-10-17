count=1
total=0
dict={
    "Maths":98,
    "English":90,
    "Gujarati":85,
    "Science":92,
    "Social Science":88
}

for i in dict:
    print(count,i,"----------",dict[i])
    count+=1
    total=total+dict[i]
    avg=total/count                           
print("total=",total)
print("avg=",avg)




