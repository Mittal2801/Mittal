#Using lambda with map
numbers = [1,2,3,4,5]
squared = list(map(lambda x : x * x,numbers))

print("Squared Numbers:",squared)

#Using lambda with filter
numbers = [1,2,3,4,5]
even_numbers = list(filter(lambda x : x % 2 == 0,numbers))

print("Even Numbers:",even_numbers)

#Using lambda with sorted
data =[('Alice',24),('dob',19),('Charlie',30)]
sorted_data = sorted(data,key = lambda x : x)

print("Sorted by Age:",sorted_data)