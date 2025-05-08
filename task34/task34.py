import random

rozmer = 5
mp = [[random.randint(-10,11) for _ in range(rozmer)] for _ in range(rozmer)]

print(mp)
counter = 0
vysyp = 0
odnies = 0
for line in mp:
    for element in line:
        counter += element
        if element < 0:
            vysyp += 1
        else:
            odnies += 1

if counter == 0:
    print("da sa to doplnit")
elif counter >0:
    print(f"musi este odniest {counter}m kopcov von z toho preistoru") 
    odnies += 1
else:
    print(f"musi este doniest {counter}m zemina do jam")
    vysyp += 1


with open("./task34/pozemok.txt", "w") as f:
    for line in mp:
        for element in line:
            f.write(f"{str(element)} ")
        f.write("\n")
    f.write(f"vysyp: {vysyp}\n")
    f.write(f"odnies: {odnies}\n")