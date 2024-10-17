import random


name=['vidhi','lalit','mansi','aditya','megha']
verb=['is','am','are','have','has']
other=['made','clever','dumb','dobo','pgl']

first=random.choice(name)
second=random.choice(verb)
third=random.choice(other)

main=first+" " + second +" " +third

print(main)