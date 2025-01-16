with open("./task2/hlasovanie_1.txt", "r") as f:
    sms = f.read().split("\n")
    print(len(sms))

with open("./task2/5220.txt", "w") as f:
    for idx, value in enumerate(sms):
        if value == "5220":
            f.write(f"{idx+1} {value}\n")

for idx, value in enumerate(sms):
    with open(f"./task2/{value}.txt", "a") as f:
        f.write(f"{idx+1}\n")
