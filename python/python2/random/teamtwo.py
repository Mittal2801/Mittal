import random

def team(players):
    random.shuffle(players)
    team1 = players[:5]
    team2 = players[5:]
    print(f"Team 1:{team1}")
    print(f"Team 2:{team2}")
    return team1,team2


players=['kohli','gill','dhoni','rohit','hardik','bumrah','k l rahul','sachin','akshar','rishabh']
team = team(players)



