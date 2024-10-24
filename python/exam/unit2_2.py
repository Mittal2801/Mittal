import array as arre
a = arre.array("i",[1, 2, 3, 4, 5])
print(a)

#update
a[2] = 40
print(a)

#slicing
a[0:2] = arre.array("i",[99, 100])
print(a)