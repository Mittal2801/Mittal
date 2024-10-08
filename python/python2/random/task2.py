import random

list=['apple','mango','grapes','pineapple','computer','cpu','keyboard','water','cricket','serial','python',
      'java','dbms','dog','vidhi','friends','flower','animal','kite','festival','program','picture','college']

word=random.choice(list)
# print(word)
# print(len(word))

for i in range(len(word)):
    print('- '*len(word))

    ch=input("Enter any character:-")

    if ch in word:
        print(ch)
        
    else:
        print("no")
else:
    print("You again try this game")