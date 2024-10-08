import random

#a string
name=random.choice("Mittal Prajapati")
print(name)

#a list
list=random.choice([45,23,78,28,30])
print(list)

#a tuple
tuple=random.choice(('apple','mango','grapes','pineapple','cherry'))
print(tuple)

#suffle() function
#arrange random order
thislist=[35,66,32,99,87]
random.shuffle(thislist)
print(thislist)

list2=['apple','cherry','pineapple','grapes','mango']
random.shuffle(list2)
print(list2)

list3=[3,'html',5,'java',9,'python',10,'dbms']
x=random.choice(list3)
print(x)

updatelist=random.sample(range(1100,1200),6)
print(updatelist)