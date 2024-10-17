import random


team=['kohli','gill','dhoni','rohit','hardik','bumrah','k l rahul','sachin','akshar','rishabh']

team_a=random.sample((team),5)
print("Team A:",team_a)

s2 = set(team)
# print(s2)

s1 = set(team_a)
# print(s1)

diff=s2.difference(s1)
# print(diff)

team_a = list(s1)
# print("Team A:",team_a)

team_b = list(diff)
print("Team B:",team_b)

# team_a=random.sample((team),5)
# li=[]

# for i in team:
#     if not i in team_a:
#         li.append(i)

# print(team_a)
# print(li)