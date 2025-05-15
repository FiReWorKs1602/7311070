with open("./task01/jump_to_distance.txt", "r") as f:
    lst = f.read().split("\n")

country = []
player_num = {}
winner = []
Max_num = " "  
for i in lst:
    country.append(i.split()[1])
    player_num[i.split()[1]] = player_num.get(i.split()[1], 0) + 1

    if Max_num < max(i.split()[2:]):
        winner = []
        Max_num = max(i.split()[2:])
        winner.append(i.split()[0])
    elif Max_num in i:
        winner.append(i.split()[0])

print(country)
print(player_num)
print(winner)
