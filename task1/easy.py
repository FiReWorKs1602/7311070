file = open("./task1/jump_to_distance.txt", "r")
data = file.read()
file.close()

# zoznam krajín
countries = []
for line in data.split("\n"):
    country = line.split()[1]
    if  country not in countries:
        countries.append(country)
print(countries)


# počty súťažiacich z jednotlivých krajín
for country in countries:
    player = data.count(country)
    print(f"V {country} je {player} hracou!")


# meno celkového víťaza
numbers = []
for word in data.split():
    if word.isdigit():
        numbers.append(word)
largest_num = max(numbers)

for player in data.split("\n"):
    if largest_num in player:
        print(player.split()[0])

