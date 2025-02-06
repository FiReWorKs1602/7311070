

file = open("./task3/hada.txt", "r")
data = file.read().split("\n")
print(len(data))
file.close()

steps_each_game = []
for hry in data:
    steps_each_game.append(len(hry))
print(max(steps_each_game))

file = open("./task3/hada.txt", "r")
for hry in file.readlines():
    hry = hry.strip() # odslanit \n
    result = ""
    count = 1

    # Prechádzame cez postupnosť, porovnávame znaky
    for i in range(1, len(hry)):
        if hry[i] == hry[i - 1]:  # Ak je znak rovnaký ako predchádzajúci
            count += 1
        else:
            # Pridáme aktuálny znak a počet do výsledku
            result += hry[i - 1] + " " + str(count) + " "
            count = 1  # Resetujeme počítadlo

    # Pridáme posledný znak a jeho počet
    result += hry[-1] + " " + str(count)
    copy = open("./task3/hada_copy.txt", "a")
    copy.write(result+"\n")
    copy.close()
file.close()