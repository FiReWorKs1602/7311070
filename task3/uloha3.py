


with open("./task3/hada.txt", "r") as file:
    data = file.read().split("\n")
    print(len(data))
    
steps_each_game = []
for hry in data:
    steps_each_game.append(len(hry))
print(max(steps_each_game))

with open("./task3/hada.txt", "r") as file:
    for player in file.readlines():
        player = player.strip()
        count = 1
        for step in range(1, len(player)):
            if player[step] == player[step-1]:
                count += 1
            else:
                copy = open("./task3/hada_copy.txt", "a")
                copy.write(f"{player[step-1]} {count} ")
                count = 1
        copy.write(f"{player[-1]} {count}\n")
