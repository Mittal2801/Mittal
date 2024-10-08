
# amount=int(input("enter amount:"))
# rate=float(input("enter rate:"))
# year=int(input("enter year:"))
# i=1

# while i<=year:
#     CI = amount * rate / 100
#     print("year",i,"Interest",CI,"total",amount+CI)
#     amount += CI
#     i += 1
    

amount=int(input("enter amount:"))
rate=float(input("enter rate:"))
year=int(input("enter year:"))
quty = year / 3

i=1

while i<=quty:
    CI=amount * rate /100
    print("month",i,"Interest",CI,"total",amount+CI)
    amount+=CI
    i+=1
    