file = open("./task4/meteo_stanice.txt", "r")
data = file.read().split("\n")
file.close()

print(len(data))

list_temp = []
train_code = []
for line in data:
    temp = line.split()[3]
    print(temp)
    list_temp.append(float(temp.strip("+").replace(",", ".")))

    code = line.split()[0]
    train_code.append(code)

highest_temp = max(list_temp)
idx = list_temp.index(highest_temp)
print(highest_temp)
print(train_code[idx])
print(sum(list_temp)/len(list_temp))
