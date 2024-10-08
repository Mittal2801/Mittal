dict={
    "rollno":"3107",
    "name":"Mittal",
    "surname":"Prajapati",
    "address":"Ahmedabad"
}


print(dict)

dict.update({"name":"vidhi"})
print(dict)


print(dict.keys())

print(dict.values())

dict.pop("surname")
print(dict)

dict.popitem()
print(dict)

dict.clear()
print(dict)