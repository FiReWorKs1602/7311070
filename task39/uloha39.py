
name_suma = input("enter name and penalty: ").split()


with open("./task39/pokuty.txt", "r") as f:
    data = [line.strip().split() for line in f.readlines()]

print(data)
isnot_in_list = True
for line in range(len(data)):
    if data[line][0] == name_suma[0]:
        data[line][1] = str(int(data[line][1])+int(name_suma[1]))
        isnot_in_list = False
if isnot_in_list:
    data.append(name_suma)
print(data)

with open("./task39/pokuty.txt", "w") as f:
    for line in data:
        if line[1] != "0":
            f.write(f"{line[0]} {line[1]}\n")
         