with open("./task2/hlasovanie_1.txt", "r") as f:
    sms = f.read().split("\n")
    print(len(sms))

for idx, value in enumerate(sms):
    with open(f"./task2/{value}.txt", "a") as f:
        f.write(f"{idx+1}\n")
