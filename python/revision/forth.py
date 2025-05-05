student= {
   'Python':91,
   "Java":70,
   'Html':95,
   'Php':80,
   'Dbms':90
}
total = 0

# for i in student:
    # print(i)
for j in student.values():
    # print(j)
    
    if j > 90:
        print(j)
        total = total+j
print("total=",total)