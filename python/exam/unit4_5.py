import datetime

 #birthday
byear = int(input("byear="))
bmonth = int(input("bmonth="))
bday = int(input("bday="))

x = datetime.datetime(byear, bmonth, bday)
print(x)
birthday = datetime.datetime.now()
print(birthday)

y = birthday - x

print(y)
