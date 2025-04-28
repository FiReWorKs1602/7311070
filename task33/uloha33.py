

with open("./task33/dopravny_prieskum.txt", "r") as f:
    data = [i.strip().split(";") for i in f.readlines()]

# 1-40 kratka, 41 - 70 standardna, 71-100 dlha
count = 0
for line in data:
    count += int(line[0])- int(line[1])
    if count <= 40:
        print(f"{line[2]}-{count}-kratka")
    elif count <= 70: 
        print(f"{line[2]}-{count}-standardna")
    else:
        print(f"{line[2]}-{count}-dlha")
print("------------------------")

# x > 10 
for line in data:
    if int(line[1]) >= 10:
        print(f"{line[2]}-automat")
    else:
        print(f"{line[2]}-no automat")

print("---------------------------")
#  x < 3
for line in data:
    if int(line[1]) <= 3:
        print(f"{line[2]}-naznamenie")
    else:
        print(f"{line[2]}-ne da znamenie")