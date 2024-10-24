list1 = [1,47,35,29,16]
f1 = open('number.txt','w')
for i in list1:
    f1.write(str(i))
    f1.write('\n')
    
    if i % 2 == 0:
        f1.write(str(i))
        f1.write("not prime")
        
    else:
        f2 = open('prime.txt','w')
        f2.write(str(i))
        f2.write('prime number')
     