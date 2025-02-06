

file = open("./task2/hlasovanie_1.txt", "r")
sms = file.read().split("\n")
print(len(sms))
file.close()

for idx, value in enumerate(sms):
    file =open(f"./task2/{value}.txt", "a")
    file.write(f"{idx+1}\n")
file.close()