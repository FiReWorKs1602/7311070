with open("./task1/jump_to_distance.txt", "r") as f:
    country = []
    player_num = {}
    winner = []
    Max_num = " "    
    lst = f.read().split("\n")
    for i in lst:
        if i.split()[1] not in country:
            country.append(i.split()[1])
            player_num[i.split()[1]] = 1
        else:
            player_num[i.split()[1]] += 1

        if Max_num < max(i.split()[2:]):
            winner = []
            Max_num = max(i.split()[2:])
            winner.append(i.split()[0])
        elif Max_num in i:
            winner.append(i.split()[0])
    
    print(country)
    print(player_num)
    print(winner)
