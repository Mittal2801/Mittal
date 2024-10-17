s1={"apple","cherry","watermelon",1,2,3}
print(s1)

s2={1,"python",2,"java",3,"php",4,"dbms"}
print(s2)

if "apple" in s1:
    print("apple is available in set")
    
for i in s2:
    print(i)
   
    
s1.add("pineapple")
print(s1)

# s2.update(s1)
# print(s2)

s1.discard("banana")
print(s1)

s2.remove("php")
print(s2)

s2.discard("dbms")
print(s2)

s1.clear()
print(s1)

# del s2
# print(s2)
