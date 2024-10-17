set1={"a","b","c","d","o","y"}
set2={"x","y","z","m","n","v","b","a","c","d","o"}


union=set1.union(set2)
print("union:",union)

intersection=set1.intersection(set2)
print("intersection:",intersection)

difference=set1.difference(set2)
print("difference:",difference)

subset=set1.issubset(set2)
print("subset:",subset)

superset=set2.issuperset(set1)
print("superset:",superset)