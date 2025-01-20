


with open("./task3/hada.txt", "r") as file:
    data = file.read()
    steps = data.split("\n")
    print(len(data.replace("\n", "")))
    

Max_s = 0
for i in range(len(steps)):
    if len(steps[i]) > Max_s:
        Max_s = len(steps[i])
        idx = i
print(idx+1)

with open("./task3/hada.txt", "r") as file:
    for player in file.readlines():
        repeat = player[0]
        count = 0
        for step in player:
            if repeat == step:
                count += 1
            else:
                copy = open("./task3/hada_copy.txt", "a")
                copy.write(f"{repeat} {count} ")
                repeat = step
                count = 1
        copy.write("\n")

        
        





