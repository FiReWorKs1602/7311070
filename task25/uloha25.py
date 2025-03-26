


with open("./task25/pacienti.txt", "r") as f:
    data = [pacient.split(" ")  for pacient in f.read().split("\n") if pacient != ""]


def Generate_BMI_list(data:list):
    BMI_result = []
    for line in data:
        BMI = round(float(line[2])/(float(line[3].replace(",", "."))**2), 1)
        BMI_result.append(BMI)
    return BMI_result

BMI_list = Generate_BMI_list(data)

with open("./task25/pacienti.txt", "w") as f:
    for idx, line in enumerate(data):
        f.write(f"{" ".join(line[:-1])} {str(BMI_list[idx])}\n")

count_obesity = 0
count_skiny = 0
for idx in range(len(BMI_list)):
    if BMI_list[idx] < 18.5:
        print(f"{data[idx][0]} - Podvaha")
        if data[idx][1][2] in "56":
            count_skiny += 1
    elif BMI_list[idx] < 25:
        print(f"{data[idx][0]} - normálna hmotnosť")
    elif BMI_list[idx] < 30:
        print(f"{data[idx][0]} - nadváha")
    else:
        print(f"{data[idx][0]} - obezita")
        count_obesity += 1

print(f"{count_obesity}-pacientov je obéznych")
print(f"{count_skiny}-zeny su podvahou")

