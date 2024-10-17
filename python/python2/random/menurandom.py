import random


starter=['paneer tikka','spring roll','cheese roll','paneer chilli','veg crispy']
main=['paneer handi','pasta','pizza','pani puri','sandwich']
desert=['ice cream','gulab jamun','pepsi','cupcake','pestry']

st = random.sample((starter),2)
print(st)

ma = random.sample((main),2)
print(ma)

de = random.sample((desert),2)
print(de)

order = st + ma + de
print("Order:-",order)