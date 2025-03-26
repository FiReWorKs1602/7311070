

with open("./task26/cyklovylety.txt", "r") as f:
    data = [line.split(" ") for line in f.read().split("\n")]

for line in data:
    hour = int(line[2])//60
    minute = round((int(line[2])/60-hour)*60)
    priemer = round(float(line[1])/(int(line[2])/60), 1)
    line[2] = f"{hour}:{minute}"
    line.insert(3,f"{priemer}")

for i in data:
    print(" ".join(i))