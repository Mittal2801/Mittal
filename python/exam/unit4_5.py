import datetime
year = int(input("year="))
month = int(input("month="))
day = int(input("day="))

birthday = datetime.datetime.now()
difference = now - birthday
print(difference.days)